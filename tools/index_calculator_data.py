"""Index decompiled definitions without running game code or evaluating C# expressions."""
from pathlib import Path
import json
import re

OUT = Path(__file__).resolve().parents[1]
SOURCE = OUT / 'source'
DATA = OUT / 'data'
DATA.mkdir(exist_ok=True)


def save(name, value):
    (DATA / name).write_text(json.dumps(value, indent=2, ensure_ascii=True) + '\n', encoding='utf-8')


def split_top(text):
    """Split commas outside strings, parentheses, braces and brackets."""
    parts, depth, start, quoted, escaped = [], 0, 0, False, False
    for i, char in enumerate(text):
        if quoted:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == '"':
                quoted = False
            continue
        if char == '"':
            quoted = True
        elif char in '({[':
            depth += 1
        elif char in ')}]':
            depth -= 1
        elif char == ',' and depth == 0:
            parts.append(text[start:i].strip())
            start = i + 1
    parts.append(text[start:].strip())
    return [p for p in parts if p]


def closing_brace(text, opening):
    depth, quoted, escaped = 0, False, False
    for i in range(opening, len(text)):
        char = text[i]
        if quoted:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == '"':
                quoted = False
            continue
        if char == '"':
            quoted = True
        elif char == '{':
            depth += 1
        elif char == '}':
            depth -= 1
            if depth == 0:
                return i
    raise ValueError('Unbalanced initializer')


translations = json.loads((DATA / 'localization.json').read_text(encoding='utf-8'))
save('localization_en-US.json', translations)


def definitions(folder, pattern):
    result = []
    for path in sorted((SOURCE / folder).glob('*.cs')):
        text = path.read_text(encoding='utf-8-sig')
        for match in re.finditer(pattern, text):
            start = text.index('{', match.start(), match.end())
            end = closing_brace(text, start)
            fields = {}
            for part in split_top(text[start + 1:end]):
                assignment = re.match(r'^(\w+)\s*=\s*(.*)$', part, re.S)
                if not assignment:
                    raise ValueError(f'Cannot index field in {path}: {part[:80]}')
                fields[assignment[1]] = assignment[2]
            identifier = match['id']
            result.append({'id': identifier, 'name': translations.get(identifier, identifier), 'definition_type': match['type'], 'source': path.relative_to(OUT).as_posix(), 'line': text[:match.start()].count('\n') + 1, 'fields_csharp': fields, 'initializer_csharp': text[start:end + 1]})
    return result


recipes = definitions('Assets.Source.Items.Recipes', r'CraftingRecipe\.Add\(new (?P<type>CraftingRecipe)\("(?P<id>[^"\n]+)"\)\s*\{')
for recipe in recipes:
    fields = recipe['fields_csharp']
    recipe['station'] = Path(recipe['source']).stem
    recipe['reagents'] = None
    recipe['results'] = None
    for field, kind, key in [('Reagents', 'CraftingReagent', 'reagents'), ('Results', 'CraftingResult', 'results')]:
        expression = fields.get(field, '')
        array = re.fullmatch(r'new ' + kind + r'\[\d+\](?:\s*\{(.*)\})?', expression, re.S)
        if array:
            entries, plain = [], True
            for entry in split_top(array[1] or ''):
                simple = re.fullmatch(r'new ' + kind + r'\("([^"\n]+)",\s*(\d+)\)', entry)
                if simple:
                    entries.append({'item': simple[1], 'count': int(simple[2])})
                else:
                    plain = False
                    break
            if plain:
                recipe[key] = entries
    recipe['simple_item_recipe'] = recipe['reagents'] is not None and recipe['results'] is not None
    recipe['base_crafting_time_seconds'] = None
    explicit_time = fields.get('CraftingTime')
    multiplier = fields.get('CraftingTimeMultiplier', '1f')
    numeric = r'\d+(?:\.\d+)?[fFdD]?'
    if explicit_time and re.fullmatch(numeric, explicit_time) and float(explicit_time.rstrip('fFdD')) != 0:
        recipe['base_crafting_time_seconds'] = float(explicit_time.rstrip('fFdD'))
    elif recipe['reagents'] is not None and re.fullmatch(numeric, multiplier):
        recipe['base_crafting_time_seconds'] = (1.5 + 0.5 * sum(r['count'] for r in recipe['reagents'])) * float(multiplier.rstrip('fFdD'))
save('recipes.json', recipes)

items = definitions('Assets.Source.Items.Impl', r'ItemType\.Add\(new (?P<type>\w+)\("(?P<id>[^"\n]+)"\)\s*\{')
save('items.json', items)

classes = {}
for path in sorted(SOURCE.rglob('*.cs')):
    text = path.read_text(encoding='utf-8-sig')
    match = re.search(r'public (?P<abstract>abstract )?class (?P<name>\w+)(?:\([^\n]*\))?\s*:\s*(?P<base>[\w.]+)', text)
    if match and path.parent.name in ('Assets.Source.Flow', 'Assets.Source.Flow.Elements'):
        classes[match['name']] = {'type': match['name'], 'base_type': match['base'], 'abstract': bool(match['abstract']), 'source': path.relative_to(OUT).as_posix(), 'line': text[:match.start()].count('\n') + 1}
nodes = []
for name, record in classes.items():
    current, chain = name, []
    while current in classes and current not in chain:
        chain.append(current)
        current = classes[current]['base_type']
    if 'FlowElement' in chain and not record['abstract']:
        text = (OUT / record['source']).read_text(encoding='utf-8-sig')
        record['inheritance'] = chain
        record['category'] = None
        for ancestor in chain:
            ancestor_text = (OUT / classes[ancestor]['source']).read_text(encoding='utf-8-sig')
            category = re.search(r'\bCategory\s*=>\s*ElementCategory\.(\w+)', ancestor_text)
            if category:
                record['category'] = category[1]
                break
        record['availability'] = 'Class present in game assembly; availability in normal gameplay is not inferred.'
        for field in ('DefaultLabel', 'Label', 'DefaultIconName', 'IconName', 'Category', 'CraftableTag', 'SupplyTag', 'RequiredTech', 'CostMultiplier', 'GoldMultiplier', 'CostCurrency'):
            found = re.search(r'\b' + field + r'\s*(?:=>|=)\s*([^;\n]+);', text)
            if found:
                record.setdefault('expressions_csharp', {})[field] = found[1].strip()
        label = record.get('expressions_csharp', {}).get('DefaultLabel', record.get('expressions_csharp', {}).get('Label', ''))
        key = re.fullmatch(r'"@([^"\n]+)"', label)
        record['name'] = translations.get(key[1], name) if key else name
        nodes.append(record)
save('nodes.json', nodes)

summary = {'nodes': len(nodes), 'recipes': len(recipes), 'simple_item_recipes': sum(r['simple_item_recipe'] for r in recipes), 'recipes_with_resolved_base_time': sum(r['base_crafting_time_seconds'] is not None for r in recipes), 'item_initializers': len(items), 'localization_entries': len(translations), 'notes': ['C# expressions are preserved as text, not evaluated.', 'Null reagent/result lists mean filters, local references, enhancements, transformations or custom callbacks; consult fields_csharp and source.', 'Items and recipes index direct Add(new ... { ... }) definitions; other runtime definitions remain in Source/.', 'Simple item recipes may still have currency costs, modifiers and side effects in fields_csharp.', 'Base crafting time uses CraftingRecipe.Add defaults; it does not include node speed, productivity, quotas, input starvation, buffers or frame timing.']}
save('index_summary.json', summary)
print(json.dumps(summary, indent=2))
