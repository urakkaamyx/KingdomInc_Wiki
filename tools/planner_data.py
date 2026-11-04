"""Extract planner metadata from the decompiled C#; never execute game code."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def split_top(text):
    parts, depth, start, quote, escaped = [], 0, 0, False, False
    for i, c in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == '"':
                quote = False
        elif c == '"':
            quote = True
        elif c in '({[':
            depth += 1
        elif c in ')}]':
            depth -= 1
        elif c == ',' and depth == 0:
            parts.append(text[start:i].strip())
            start = i + 1
    parts.append(text[start:].strip())
    return [p for p in parts if p]


def block_end(text, start):
    depth, quote, escaped = 0, False, False
    for i in range(start, len(text)):
        c = text[i]
        if quote:
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == '"':
                quote = False
        elif c == '"':
            quote = True
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return i
    raise ValueError('Unbalanced C# initializer')


def literal(expr, default=None):
    if expr and re.fullmatch(r'"[^"\n]*"', expr):
        return expr[1:-1]
    return default


def snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def numeric(expr, default):
    try:
        return float((expr or '').rstrip('fFdDlL'))
    except ValueError:
        return default


def build_planner_data(items, names, icon, currencies):
    techs, buildings = {}, {}
    node_index = json.loads((ROOT / 'data' / 'nodes.json').read_text(encoding='utf-8'))
    for node in node_index:
        text = (ROOT / node['source']).read_text(encoding='utf-8-sig')
        expressions = node.get('expressions_csharp', {})
        tech = literal(expressions.get('RequiredTech'), snake(node['type']))
        rate = re.search(r'OutputPerSecond\s*=>\s*(\d+(?:\.\d+)?)[fF]?\s*\*\s*Speed', text)
        buildings[node['type']] = {'id': node['type'], 'tech': tech, 'name': node['name'], 'icon': icon(expressions.get('DefaultIconName') or expressions.get('IconName')), 'category': node['category'], 'baseRate': float(rate[1]) if rate else 1.0, 'qualityType': 'Artisan', 'resourceTag': (expressions.get('SupplyTag') or '').replace('ResourceTag.', ''), 'source': node['source'], 'standardUpgrades': False}
    if 'AdventurersGuild' in buildings:
        buildings['AdventurersGuild']['baseRate'] = 0.5
        buildings['AdventurersGuild']['warGate'] = 'forest:4'
    if 'Farm' in buildings:
        buildings['Farm']['warGate'] = 'eastern:1'

    def add(record):
        previous = techs.get(record.get('previous'))
        root = record.get('root') or (previous.get('root') if previous else None)
        if root:
            record['root'] = root
        parent = previous or techs.get(root)
        record['tier'] = record.get('tier') or (parent['tier'] if parent else 0)
        record['requires'] = list(dict.fromkeys(filter(None, [root, record.get('previous'), *record.get('additional', [])])))
        record.setdefault('grants', [])
        record.setdefault('resourceGrants', [])
        techs[record['id']] = record

    def helper(kind, building, path, line, quality_type=None):
        base = buildings[building]['tech'] if building in buildings else snake(building)
        source = 'source/Assets.Source.Player/TechNodeHelper.cs'
        base_tier = techs.get(base, {}).get('tier', 1)
        helper_text = (ROOT / source).read_text(encoding='utf-8-sig')
        helper_match = re.search(r'public static TechNode ' + re.escape(kind) + r'\(', helper_text)
        helper_line = helper_text[:helper_match.start()].count('\n') + 1 if helper_match else 1
        common = {'type': 'UpgradeSlot', 'source': source, 'line': helper_line, 'generated': True, 'building': building, 'callSource': path.relative_to(ROOT).as_posix(), 'callLine': line}
        if kind == 'UpgradeWorker':
            record = {'id': base + '_automation', 'root': base, 'tier': base_tier, 'name': names.get(base + '_automation', f'{buildings.get(building, {}).get("name", building)} automation'), 'icon': icon('Icons_17'), 'slotCount': 1, 'addon': 'Worker'}
        elif kind == 'UpgradeSlot2':
            tier = max(techs.get(base + '_automation', {}).get('tier', base_tier) + 1, 3)
            extra = ['war_effort']
            if tier == 2:
                extra.append('requisition_office')
            elif 5 <= tier <= 7:
                extra.append('quest_board')
            elif 8 <= tier <= 15:
                extra.append('dungeon')
            record = {'id': base + '_automation_2', 'previous': base + '_automation', 'tier': tier, 'additional': extra, 'name': f'{buildings.get(building, {}).get("name", building)} · second add-on slot', 'icon': icon('Icons_18'), 'slotCount': 2}
        elif kind == 'UpgradeSlot3':
            tier = max(techs.get(base + '_automation_2', {}).get('tier', base_tier + 1) + 1, 7)
            record = {'id': base + '_automation_3', 'previous': base + '_automation_2', 'additional': ['dungeon'], 'tier': tier, 'name': f'{buildings.get(building, {}).get("name", building)} · third add-on slot', 'icon': icon('Icons2_77'), 'slotCount': 3}
        elif kind == 'UpgradeQuality':
            tier = max(techs.get(base + '_automation_2', {}).get('tier', base_tier + 1) + 1, 4)
            quality_type = quality_type or 'Artisan'
            record = {'id': base + '_quality', 'previous': base + '_automation_2', 'tier': tier, 'name': f'{buildings.get(building, {}).get("name", building)} · artisans', 'icon': icon('Icons_118'), 'addon': quality_type, 'warGate': 'forest:2', 'conditionText': names.get('QualityRequiresWar', 'Complete Forest war stage 2')}
        elif kind == 'UpgradeProductivity':
            tier = max(techs.get(base + '_automation', {}).get('tier', base_tier) + 1, 4)
            record = {'id': base + '_productivity', 'previous': base + '_automation', 'additional': ['war_effort'], 'tier': tier, 'name': f'{buildings.get(building, {}).get("name", building)} · overseers', 'icon': icon('Icons2_76'), 'addon': 'Overseer'}
        elif kind == 'UpgradeCoffers':
            record = {'id': base + '_coffers', 'previous': base + '_automation_2', 'additional': ['war_effort'], 'tier': 3, 'name': f'{buildings.get(building, {}).get("name", building)} coffers', 'icon': icon('Icons_120'), 'addon': 'Coffers'}
        else:
            return
        add({**common, **record})

    tech_source = (ROOT / 'source/Assets.Source.Player/TechNode.cs').read_text(encoding='utf-8')
    file_order = re.findall(r'new (T\w+)\(\);', tech_source)
    for file_name in file_order:
        path = ROOT / 'source/Assets.Source.Player.Tech' / (file_name + '.cs')
        text = path.read_text(encoding='utf-8-sig')
        pattern = r'new TechNode\("(?P<id>[^"\n]+)"\)\s*\{|TechNodeHelper\.(?P<helper>AddDefaultUpgrades|UpgradeWorker|UpgradeSlot2|UpgradeSlot3|UpgradeQuality|UpgradeProductivity|UpgradeCoffers)\((?P<args>[^;]*?)\)'
        for match in re.finditer(pattern, text):
            line = text[:match.start()].count('\n') + 1
            if match['helper']:
                args = split_top(match['args'])
                building = literal(args[0])
                quality = next((literal(arg.split(':', 1)[-1].strip()) for arg in args[1:] if literal(arg.split(':', 1)[-1].strip())), None)
                if match['helper'] == 'AddDefaultUpgrades':
                    if building in buildings:
                        buildings[building]['qualityType'] = quality or 'Artisan'
                        buildings[building]['standardUpgrades'] = True
                    for kind in ('UpgradeWorker', 'UpgradeSlot2', 'UpgradeProductivity', 'UpgradeQuality', 'UpgradeSlot3'):
                        helper(kind, building, path, line, quality)
                else:
                    helper(match['helper'], building, path, line, quality)
                continue
            start = match.end() - 1
            end = block_end(text, start)
            fields = {}
            for part in split_top(text[start + 1:end]):
                found = re.match(r'^(\w+)\s*=\s*(.*)$', part, re.S)
                if found:
                    fields[found[1]] = found[2]
            identifier = match['id']
            custom = fields.get('CustomRequirement', '')
            war = re.search(r'HasWarStage\("([^"\n]+)",\s*(\d+)\)', custom)
            raw_name = literal(fields.get('Name'), '@' + identifier)
            name = names.get(raw_name[1:], raw_name[1:].replace('_', ' ').title()) if raw_name.startswith('@') else raw_name
            # Some translated descriptions contain tokens replaced by game code; preserve them rather than execute them.
            add({'id': identifier, 'name': name, 'type': fields.get('NodeType', 'TechNodeType.Utility').replace('TechNodeType.', ''), 'tier': int(numeric(fields.get('CostTier'), 0)), 'root': literal(fields.get('Root')), 'previous': literal(fields.get('Previous')), 'additional': re.findall(r'"([^"\n]+)"', fields.get('AdditionalRequirements', '')), 'grants': re.findall(r'\.AddTech\("([^"\n]+)"', fields.get('OnUnlock', '')), 'resourceGrants': [{'item': item, 'rate': float(rate)} for item, rate in re.findall(r'\.AddResource\("([^"\n]+)",\s*(\d+(?:\.\d+)?)\)', fields.get('OnUnlock', ''))], 'icon': icon(fields.get('IconName')), 'dev': fields.get('DevMode') == 'true', 'hidden': fields.get('Hidden') == '(GamePlayer ply) => true', 'warGate': f'{war[1]}:{war[2]}' if war else None, 'conditionKey': 'condition:' + identifier if custom and not war else None, 'conditionText': names.get(literal(fields.get('CustomRequirementDesc'), '').lstrip('@'), custom), 'source': path.relative_to(ROOT).as_posix(), 'line': line})
            techs[identifier]['unlocksItems'] = re.findall(r'\.UnlockItem\(ItemType\.Get\("([^"\n]+)"', fields.get('OnUnlock', ''))
        for identifier in re.findall(r'TechNode\.Get\("([^"\n]+)"\)\.Hidden = \(GamePlayer ply\) => true', text):
            if identifier in techs:
                techs[identifier]['hidden'] = True

    # Resource unlocks and base supply sources, including forest and campaign-gated resource nodes.
    resource_techs = {t['id'] for t in techs.values() if t['type'] == 'Resource'}
    resource_sources = []
    for identifier, item in items.items():
        fields = item['fields_csharp']
        tag = fields.get('Tag', '').replace('ResourceTag.', '')
        building = next((b for b in buildings.values() if b['resourceTag'] and b['resourceTag'] == tag), None)
        if item['definition_type'] == 'ForestItemType':
            building = buildings.get('Forest')
        elif item['definition_type'] == 'FarmItemType':
            building = buildings.get('Farm')
        if not building:
            continue
        prefix = {'Mine': 'mine', 'SupplyDepot': 'supply', 'Forest': 'forest', 'Farm': 'farm', 'AdventurersGuild': 'recruit', 'Barracks': 'recruit', 'AdventureSupplies': 'supply'}.get(building['id'], building['tech'])
        candidate_ids = [prefix + '_' + identifier, building['tech'] + '_' + identifier, identifier]
        unlock = next((candidate for candidate in candidate_ids if candidate in resource_techs), None)
        if not unlock:
            # The unlock's AddResource callback is definitive when naming is irregular.
            unlock = next((t['id'] for t in techs.values() if identifier in t.get('unlocksItems', []) or any(g['item'] == identifier for g in t['resourceGrants'])), building['tech'])
        resource_sources.append({'id': 'resource:' + identifier, 'item': identifier, 'station': building['id'], 'tech': unlock, 'time': 1 / building['baseRate'], 'quotaStep': numeric(fields.get('QuotaAmount'), 1.0), 'quotaKind': 'forest' if building['id'] == 'Forest' else ('farm' if building['id'] == 'Farm' else 'resource'), 'workerType': fields.get('WorkerType', '').replace('ForestWorker.', ''), 'workersPerItem': numeric(fields.get('WorkersPerItem'), 1), 'costs': currencies(fields.get('ResourceCost') or fields.get('HarvestCost')), 'qualityValue': numeric(fields.get('ResourceValue'), 0), 'source': item['source'], 'line': item['line']})

    missing = sorted({req for tech in techs.values() for req in tech['requires'] if req not in techs})
    if missing:
        raise ValueError(f'Unresolved technology prerequisites: {missing}')
    result = {'techs': list(techs.values()), 'buildings': buildings, 'resourceSources': resource_sources, 'initialTech': ['mine', 'forge', 'iron_ingot'], 'initialQuotas': {'iron_ore': 1}, 'warStages': [{'id': region, 'name': region.title() + ' campaign', 'max': 4} for region in ('forest', 'eastern', 'yensburg', 'north')], 'notes': ['Research prices are not modeled.', 'Custom campaign conditions require explicit configuration.', 'Technology dependency and upgrade metadata was extracted from TechNode classes and TechNodeHelper; UI layout is not reproduced.']}
    (ROOT / 'data/planner_rules.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    return result
