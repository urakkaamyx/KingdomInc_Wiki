"""Rebuild the wiki from the installed assembly's ILSpy source, without loading game code."""
from pathlib import Path
from collections import Counter, defaultdict
import re, json, hashlib, shutil, sys, html

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT.parent
SRC = ROOT / 'source'
DIST = ROOT / 'dist'
DATA = ROOT / 'data'
sys.path.insert(0, str(ROOT / 'tools'))
from planner_data import split_top, block_end, build_planner_data

def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

names = json.loads((DATA / 'localization.json').read_text(encoding='utf-8'))
installed_hash = hashlib.sha256((GAME/'KingdomInc_Data/Managed/Assembly-CSharp.dll').read_bytes()).hexdigest()
manifest = json.loads((ROOT/'source-manifest.json').read_text(encoding='utf-8'))
assert manifest['assemblySha256'] == installed_hash, 'Game assembly changed: regenerate source and localization before rebuilding.'
files = {p.relative_to(SRC).as_posix(): p.read_text(encoding='utf-8-sig') for p in sorted(SRC.rglob('*.cs'))}
articles = []
byid = {}
coverage = defaultdict(set)

def words(s):
    s = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', ' ', s).replace('_', ' ')
    return s[:1].upper() + s[1:]

def clean(s):
    # Unity formatting is not HTML, and translation replacement tokens remain visible.
    text = re.sub(r'</?(?:color|size|b|i|sprite|link)(?:=[^>]*)?>', '', str(s)).replace('\\n', '\n')
    return re.sub(r'#([^#\n]+)#', r'\1', text)

def tr(s):
    s = str(s)
    s = s[1:] if s.startswith('@') else s
    return clean(names.get(s, words(s)))

def lit(s):
    return s[1:-1] if s and re.fullmatch(r'"[^"\n]*"', s) else None

def fields(block):
    result = {}
    for p in split_top(block):
        m = re.match(r'^(\w+)\s*=\s*(.*)$', p, re.S)
        if m: result[m[1]] = m[2].strip()
    return result

def line_at(text, offset): return text[:offset].count('\n') + 1
def source(path, line=1): return {'path': path.removeprefix('source/').removeprefix('Source/'), 'line': line}
def ref(identifier, label=None): return {'id': identifier, 'label': label or identifier}

def section(title, paragraphs=None, headers=None, rows=None, code=None):
    s = {'title': title}
    if paragraphs: s['paragraphs'] = paragraphs
    if rows: s['table'] = {'headers': headers, 'rows': rows}
    if code: s['code'] = code
    return s

def add(identifier, title, category, summary, sections, sources, **extra):
    assert identifier not in byid, f'Duplicate page: {identifier}'
    a = dict(id=identifier, title=clean(title), category=category, summary=clean(summary), sections=sections,
             sources=[source(s['path'], s.get('line', 1)) for s in sources], **extra)
    byid[identifier] = a
    articles.append(a)
    for s in a['sources']: coverage[s['path']].add(identifier)
    return a

def definitions(folder, pattern):
    for path, text in files.items():
        if not path.startswith(folder + '/'): continue
        for m in re.finditer(pattern, text):
            start = m.end() - 1
            end = block_end(text, start)
            yield {'id': m['id'], 'fields': fields(text[start+1:end]), 'path': path,
                   'line': line_at(text, m.start()), 'block': text[start+1:end], 'offset': m.start(),
                   'kind': m.groupdict().get('kind', '')}

def numeric(expr):
    if expr and re.fullmatch(r'-?\d+(?:\.\d+)?[fFdDlL]?', expr): return float(expr.rstrip('fFdDlL'))
    return None

def pretty_num(n): return f'{n:g}'

def stat_rows(expr):
    return [[words(k), v] for k, v in re.findall(r'EquipStat\.(\w+)\s*,\s*(?:amt:\s*)?(-?\d+(?:\.\d+)?)', expr or '')]

def currency_text(expr):
    pairs = re.findall(r'Currency\.(\w+)\s*,\s*(-?\d+)[Ll]?', expr or '')
    chunks=[]
    for c,n in pairs:
        amount=int(n)
        if c=='Gold':
            magnitude=abs(amount);gold=magnitude//10000;silver=magnitude//100%100;copper=magnitude%100
            display=' '.join(f'{value} {label}' for value,label in [(gold,'gold'),(silver,'silver'),(copper,'copper')] if value) or '0 copper'
            chunks.append(('-' if amount<0 else '')+display+f' ({amount:,} base coin units)')
        else:chunks.append(f'{amount:,} {tr("Currency"+c)}')
    return ', '.join(chunks)

def description(identifier, f=None):
    val = lit((f or {}).get('Description', ''))
    key = (val or ('@' + identifier + '_desc')).lstrip('@')
    return clean(names.get(key, ''))

def field_rows(f, skip=()):
    rows=[]
    for k,v in f.items():
        if k in skip or k in ('IconName','RelativePosition','AbsolutePosition','EnemySprites','Icon','Position'):continue
        val=lit(v)
        if val is not None:
            v = tr(val) if val.startswith('@') else val
        elif numeric(v) is not None: v=pretty_num(numeric(v))
        elif re.fullmatch(r'\w+\.\w+',v):v=words(v.split('.')[-1])
        elif len(v)>200 or '=>' in v or '{' in v:continue
        rows.append([words(k),v])
    return rows

items = json.loads((DATA / 'items.json').read_text(encoding='utf-8'))
recipes = json.loads((DATA / 'recipes.json').read_text(encoding='utf-8'))
nodes = json.loads((DATA / 'nodes.json').read_text(encoding='utf-8'))
itemmap = {r['id']:r for r in items}

def currencies(expr):
    return [{'currency':c,'amount':int(n)} for c,n in re.findall(r'Currency\.(\w+)\s*,\s*(\d+)[Ll]?',expr or '')]

planner = build_planner_data(itemmap, names, lambda x: (lit(x) or x or '').removeprefix('@'), currencies)
techmap={r['id']:r for r in planner['techs']}
buildingmap=planner['buildings']
enhancements=list(definitions('Assets.Source.Items.Enhancements',r'new (?P<kind>ItemEnhancement)\("(?P<id>[^"]+)"\)\s*\{'))
enhmap={e['id']:e for e in enhancements}
questdefs=list(definitions('Assets.Source.Adventure.Quests',r'new (?P<kind>Quest)\("(?P<id>[^"]+)"\)\s*\{'))

item_recipes=defaultdict(list)
item_uses=defaultdict(list)
for r in recipes:
    for pair in r.get('results') or []:item_recipes[pair['item']].append(r)
    for pair in r.get('reagents') or []:item_uses[pair['item']].append(r)

icons={}
icon_dir=DIST/'assets'/'icons'
icon_dir.mkdir(parents=True,exist_ok=True)
for p in sorted((GAME/'Extracted'/'Exports'/'Sprite').rglob('*.png')):
    key=p.stem.split('__',1)[-1]
    if re.fullmatch(r'(?:Icons\d*|AnimationFrames)_\d+',key) and key not in icons:
        target=icon_dir/(key+'.png');shutil.copy2(p,target);icons[key]='assets/icons/'+key+'.png'

def item_link(identifier):
    if identifier in itemmap:return ref('item:'+identifier,tr(identifier))
    if identifier in enhmap:return ref('enhancement:'+identifier,tr(identifier))
    return tr(identifier)

for r in items:
    identifier=r['id'];f=r['fields_csharp']; kind=r['definition_type']
    s=[]
    desc=description(identifier,f)
    if desc:s.append(section('In the game',[desc]))
    rows=[['Item ID',identifier],['Item type',words(kind.replace('ItemType','')) or 'Item']]+field_rows(f,('BaseStats','Traits','Advancements','Description','DisplayName','Stats','EquipTrait'))
    s.append(section('Reference values',headers=['Property','Value'],rows=rows))
    stats=stat_rows(f.get('BaseStats'))
    if stats:s.append(section('Base stats',['These are definition values before quality, training, equipment, enhancements and active traits.'],['Stat','Base amount'],stats))
    traits=[x for x in re.findall(r'AdventurerTrait\.(\w+)',f.get('Traits','')+' '+f.get('EquipTrait','')) if x!='Resist']
    if traits:s.append(section('Traits',headers=['Trait'],rows=[[ref('trait:'+t,words(t))] for t in dict.fromkeys(traits)]))
    if 'ResourceValue' in f or kind in ('ForestItemType','FarmItemType'):
        srcs=[x for x in planner['resourceSources'] if x['item']==identifier]
        if srcs:s.append(section('Gathering',headers=['Building','Research','Quota step'],rows=[[ref('building:'+x['station'],buildingmap[x['station']]['name']),ref('tech:'+x['tech'],tr(x['tech'])),x['quotaStep']] for x in srcs]))
    if item_recipes[identifier]:s.append(section('Produced by',headers=['Recipe','Station','Base seconds'],rows=[[ref('recipe:'+x['id'],tr(x['id'])),ref('building:'+x['station'],words(x['station'])),x['base_crafting_time_seconds'] if x['base_crafting_time_seconds'] is not None else 'Custom'] for x in item_recipes[identifier]]))
    if item_uses[identifier]:s.append(section('Used in',headers=['Recipe','Units per batch'],rows=[[ref('recipe:'+x['id'],tr(x['id'])),sum(y['count'] for y in x['reagents'] if y['item']==identifier)] for x in item_uses[identifier]]))
    if 'Advancements' in f:
        adv=[]
        for m in re.finditer(r'new AdventurerAdvancement\s*\{',f['Advancements']):
            start=m.end()-1;end=block_end(f['Advancements'],start);af=fields(f['Advancements'][start+1:end])
            target=re.search(r'ChangeItemType\("([^"]+)"',af.get('Apply',''))
            adv.append([item_link(target[1]) if target else tr(lit(af.get('DisplayName')) or 'Advancement'),words(af.get('Source','').split('.')[-1]),af.get('Available','See advancement implementation')])
        if adv:s.append(section('Class advancement',['Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.'],['Result','Where','Requirement'],adv))
    sources=[source(r['source'],r['line'])]
    add('item:'+identifier,tr(identifier),'Classes' if kind in ('AdventurerItemType','HumanItemType','CombatantItemType') else 'Items',
        desc or f'{tr(identifier)} is a {words(kind.replace("ItemType", "")).lower() or "crafting"} item in the installed game.',s,sources,icon=lit(f.get('IconName')),technical=f)

def parse_recipe_entries(r,key):
    expr=r['fields_csharp'].get(key,'');kind='CraftingReagent' if key=='Reagents' else 'CraftingResult'
    array=re.search(r'new '+kind+r'\[\d+\]\s*(?:\{(.*)\})?',expr,re.S)
    if not array:return []
    entries=split_top(array[1] or '')
    rows=[];whole=files[r['source'].removeprefix('source/')]
    for entry in entries:
        transform = re.search(r'CraftingResult.TransformAdventurer\((\d+),\s*"([^"]+)"\)',entry)
        if transform:
            rows.append([item_link(transform[2]),'Transforms adventurer from input '+transform[1]])
            continue
        if re.fullmatch(r'\w+',entry):
            match=re.search(r'\b'+re.escape(entry)+r'\s*=\s*(new '+kind+r'\(.*?);',whole,re.S)
            if match:entry=match[1]
        m=re.match(r'new '+kind+r'\((.*)\)',entry,re.S)
        if not m:rows.append(['Custom selection',entry]);continue
        args=split_top(m[1]);first=lit(args[0]);amt=args[1] if len(args)>1 else '1'
        if first:
            label=item_link(first)
            if key == 'Results' and re.fullmatch(r'\d*\.\d+f',amt):
                amt = '1 item at '+pretty_num(float(amt[:-1])*100)+'% probability'
            rows.append([label,amt])
        else:
            friendly=lit(args[3]) if len(args)>3 else None
            rows.append([tr(friendly) if friendly else 'Conditional item / transformation',amt])
    return rows

for r in recipes:
    identifier=r['id'];f=r['fields_csharp'];s=[];desc=description(identifier,f)
    if desc:s.append(section('In the game',[desc]))
    time=r['base_crafting_time_seconds']
    if time is None:
        ingredients=parse_recipe_entries(r,'Reagents')
        amounts=[numeric(str(x[1])) for x in ingredients]
        multiplier=numeric(f.get('CraftingTimeMultiplier','1f'))
        explicit=numeric(f.get('CraftingTime'))
        if explicit is not None and explicit!=0:time=explicit
        elif all(x is not None for x in amounts) and multiplier is not None:
            time=(1.5+0.5*sum(amounts))*multiplier
    rows=[['Station',ref('building:'+r['station'],words(r['station']))],['Base crafting time',f'{time:g} seconds' if time is not None else 'Uses a custom input, filter or callback; see mechanics and implementation fields.'],['Research',ref('tech:'+identifier,tr(identifier)) if identifier in techmap else 'Resolved by recipe RequiredTech in the game']]
    if f.get('CraftingCost'):rows.append(['Currency consumed per batch',currency_text(f['CraftingCost']) or 'Dynamic cost; see implementation'])
    if f.get('CraftingReward'):rows.append(['Currency reward per batch',currency_text(f['CraftingReward']) or 'Dynamic reward; see implementation'])
    if 'BaseProductivity' in f:rows.append(['Base productivity modifier',f['BaseProductivity']])
    s.append(section('Crafting', ['Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.'], ['Property','Value'],rows))
    for key,title in [('Reagents','Ingredients'),('Results','Results')]:
        rs=parse_recipe_entries(r,key)
        if rs:s.append(section(title,headers=['Item or selection','Count / rule'],rows=rs))
        elif key=='Reagents':s.append(section(title,['No item ingredients in the declared array. Currency costs and custom callbacks can still apply.']))
    if 'OnFinished' in f:s.append(section('Special processing',['This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.']))
    add('recipe:'+identifier,tr(identifier)+' recipe','Recipes',desc or f'Craft {tr(identifier)} at the {words(r["station"])}.',s,[source(r['source'],r['line']),source('Assets.Source.Items/CraftingRecipe.cs',1)],icon=lit(f.get('IconName')) or lit(itemmap.get(identifier,{}).get('fields_csharp',{}).get('IconName')),technical=f)

for r in enhancements:
    f=r['fields'];identifier=r['id'];s=[]
    desc=description(identifier,f)
    if desc:s.append(section('Effect',[desc]))
    rows=stat_rows(f.get('Stats'))
    if rows:s.append(section('Base stat modifiers',['Enhancement quality and application rules determine the final contribution.'],['Stat','Amount at definition quality'],rows))
    rs=field_rows(f,('Stats','DisplayName','Description','Trait'))
    if rs:s.append(section('Properties',headers=['Property','Value'],rows=rs))
    trait=re.findall(r'AdventurerTrait\.(\w+)',f.get('EquipTrait',''))
    if trait:s.append(section('Applied traits',headers=['Trait'],rows=[[ref('trait:'+t,words(t))] for t in trait]))
    producing=[x for x in recipes if re.search(r'new CraftingResult\("'+re.escape(identifier)+r'"\)',x['fields_csharp'].get('Results',''))]
    if producing:s.append(section('Application recipes',headers=['Recipe','Station'],rows=[[ref('recipe:'+x['id'],tr(x['id'])),ref('building:'+x['station'],words(x['station']))] for x in producing]))
    add('enhancement:'+identifier,tr(identifier),'Enhancements',desc or f'{tr(identifier)} is an equipment or item enhancement.',s,[source(r['path'],r['line'])],icon=lit(f.get('IconName')),technical=f)

for r in planner['techs']:
    identifier=r['id'];s=[];rows=[['Internal ID',identifier],['Type',words(r['type'])],['Cost tier',r['tier']]]
    if r.get('dev'):rows.append(['Availability','Developer mode'])
    if r.get('hidden'):rows.append(['Visibility','Hidden by code'])
    desc=description(identifier)
    if desc:s.append(section('Research effect',[desc]))
    s.append(section('Research data',headers=['Property','Value'],rows=rows))
    if r['requires']:s.append(section('Prerequisites',headers=['Required research'],rows=[[ref('tech:'+x,tr(x))] for x in r['requires']]))
    if r.get('conditionText'):s.append(section('Additional condition',[clean(r['conditionText'])]))
    if r.get('warGate'):s.append(section('Campaign condition',[r['warGate']+' (campaign ID : completed stage)']))
    grants=r.get('grants',[])
    if grants:s.append(section('Also grants research',headers=['Unlocked automatically'],rows=[[ref('tech:'+x,tr(x)) if x in techmap else tr(x)] for x in grants]))
    if r.get('resourceGrants'):s.append(section('Resource quota granted',headers=['Resource','Amount'],rows=[[item_link(x['item']),x['rate']] for x in r['resourceGrants']]))
    if identifier in itemmap:s.append(section('Related item',headers=['Item'],rows=[[item_link(identifier)]]))
    if any(x['id']==identifier for x in recipes):s.append(section('Related recipe',headers=['Recipe'],rows=[[ref('recipe:'+identifier,tr(identifier))]]))
    dependents=[x for x in planner['techs'] if identifier in x['requires']]
    if dependents:s.append(section('Leads to',headers=['Research'],rows=[[ref('tech:'+x['id'],x['name'])] for x in dependents]))
    direct=None
    if not r.get('generated'):
        text=files[r['source'].removeprefix('source/')];m=re.search(r'new TechNode\("'+re.escape(identifier)+r'"\)\s*\{',text)
        if m:direct=fields(text[m.end():block_end(text,m.end()-1)])
    tech_sources=[source(r['source'],r['line']),source('Assets.Source.Player/TechNode.cs',1)]
    if r.get('callSource'):tech_sources.append(source(r['callSource'],r['callLine']))
    add('tech:'+identifier,r['name'],'Research',desc or f'{r["name"]} is a tier {r["tier"]} {words(r["type"]).lower()} research node.',s,tech_sources,icon=r.get('icon'),technical=direct or {'GeneratedBy':'TechNodeHelper','Model':json.dumps(r,ensure_ascii=False)})

# All concrete flow classes, including developer utilities, receive their own reference.
for r in nodes:
    name=r['type'];p=r['source'].removeprefix('source/');text=files[p];s=[]
    stringprops={}
    for m in re.finditer(r'\b(\w+)\s*(?:=>|=)\s*("[^"\n]*");',text):stringprops[m[1]]=lit(m[2])
    desc=tr(stringprops['Description']) if stringprops.get('Description') else ''
    if desc:s.append(section('Purpose',[desc]))
    rs=[['Type',name],['Category',r['category'] or 'Unspecified'],['Inheritance',' → '.join(r['inheritance'])]]
    required=stringprops.get('RequiredTech')
    if required:rs.append(['Research required',ref('tech:'+required,tr(required)) if required in techmap else required])
    if name in ('DevSpawner','DemoTurtle'):rs.append(['Availability','Developer / demonstration class; normal-game availability is not established'])
    s.append(section('Building reference',headers=['Property','Value'],rows=rs))
    recipe_list=[x for x in recipes if x['station']==name]
    if recipe_list:s.append(section('Recipes',headers=['Recipe','Base seconds'],rows=[[ref('recipe:'+x['id'],tr(x['id'])),x['base_crafting_time_seconds'] if x['base_crafting_time_seconds'] is not None else 'Custom'] for x in recipe_list]))
    gathered=[x for x in planner['resourceSources'] if x['station']==name]
    if gathered:s.append(section('Resource selections',headers=['Resource','Unlock'],rows=[[item_link(x['item']),ref('tech:'+x['tech'],tr(x['tech']))] for x in gathered]))
    upgrades=[x for x in planner['techs'] if x.get('building')==name]
    if upgrades:s.append(section('Upgrade research',headers=['Research','Tier'],rows=[[ref('tech:'+x['id'],x['name']),x['tier']] for x in upgrades]))
    declarations=[]
    for m in re.finditer(r'^\s*public (?:override |virtual |static |readonly |const )*(?:[\w<>,\[\]?]+) (\w+)\s*=>\s*([^;\n]+);',text,re.M):
        if len(m[2])<220:declarations.append([words(m[1]),tr(lit(m[2])) if lit(m[2]) else m[2]])
    if declarations:s.append(section('Declared behavior values',headers=['Property','Definition'],rows=declarations))
    add('building:'+name,r['name'],'Buildings',desc or f'{r["name"]} is a {words(r["category"] or "utility").lower()} flow element.',s,[source(p,r['line'])],icon=stringprops.get('DefaultIconName') or stringprops.get('IconName'),technical={'Source class':name,'Inherited behavior':' → '.join(r['inheritance'])})

def rewards(expr):
    rows=[]
    for typ,args in re.findall(r'new (\w+Reward)\(([^\n;]+?)\)',expr or ''):
        a=split_top(args)
        if typ=='CurrencyReward' and len(a)>=2:rows.append([words(a[0].split('.')[-1]),a[1], 'Currency'])
        elif typ=='ItemReward' and a:
            rows.append([item_link(lit(a[0]) or a[0]),a[2] if len(a)>2 else '1',f'Base quality {a[1]}' if len(a)>1 else 'Base quality 1'])
        else:rows.append([words(typ),', '.join(a),'Special reward'])
    return rows

for r in questdefs:
    f=r['fields'];identifier=r['id'];s=[];desc=description(identifier,f)
    if desc:s.append(section('Objective',[desc]))
    rows=field_rows(f,('FirstRewards','RepeatableRewards','Challenges','OnComplete','DisplayName','Description'))
    for k,default in [('EnergyPerTick','0.2f (default)'),('TrainingAdded','0.12f (default)')]:
        if k not in f:rows.append([words(k),default])
    s.append(section('Quest parameters',['Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.'],['Property','Value'],rows))
    challenge_ids=re.findall(r'QuestChallenge\.(\w+)',f.get('Challenges',''))
    if challenge_ids:s.append(section('Challenges',headers=['Challenge'],rows=[[ref('challenge:'+x,words(x))] for x in challenge_ids]))
    for k,t in [('FirstRewards','First completion rewards'),('RepeatableRewards','Repeat rewards')]:
        rs=rewards(f.get(k,''))
        s.append(section(t,headers=['Reward','Amount','Rule'],rows=rs) if rs else section(t,['No reward entries in this definition. Completion callbacks may have separate effects.']))
    if f.get('OnComplete'):s.append(section('Completion effect',['This quest has a completion callback, such as class advancement. Its exact rule is included in the implementation fields.']))
    add('quest:'+identifier,tr(identifier),'Quests',desc or f'{tr(identifier)} is a quest available through the quest board.',s,[source(r['path'],r['line'])],icon=lit(f.get('IconName')),technical=f)

# Named static trait and challenge declarations have no string constructor IDs.
for folder,filename,kind,cat in [('Assets.Source.Adventure','AdventurerTrait.cs','AdventurerTrait','Traits'),('Assets.Source.Adventure','QuestChallenge.cs','QuestChallenge','Challenges'),('Assets.Source.Player','PrestigeNode.cs','PrestigeNode','Prestige')]:
    path=folder+'/'+filename;text=files[path]
    pattern=r'public static (?:readonly )?'+kind+r' (?P<id>\w+)\s*=\s*new '+kind+r'(?:\("[^"]+"\))?\s*\{'
    for m in re.finditer(pattern,text):
        st=m.end()-1;end=block_end(text,st);f=fields(text[st+1:end]);identifier=m['id'];prefix={'Traits':'trait','Challenges':'challenge','Prestige':'prestige'}[cat]
        title=tr(lit(f.get('DisplayName')) or lit(f.get('Label')) or words(identifier))
        desc=description(identifier,f)
        if cat=='Prestige':
            match=re.search(r'new PrestigeNode\("([^"]+)"\)',m[0]);key=match[1] if match else identifier
            title=tr('prestige_'+key);desc=description('prestige_'+key)
        ss=[]
        if desc:ss.append(section('Effect',[desc]))
        if cat=='Prestige':
            rank_values={
                'TechCostReduce':lambda n:0.5+0.05*(n-1),
                'ResourceCostReduce':lambda n:0.05+0.02*(n-1),
                'CurrencyTaxReduce':lambda n:0.25+0.05*(n-1),
                'EquipmentQuality':lambda n:0.02*n,
                'HumanQuality':lambda n:0.02*n,
                'HandcraftingProductivity':lambda n:1+0.25*(n-1),
                'DarkEssenceQuality':lambda n:0.1+0.05*(n-1),
                'HumanHealth':lambda n:0.05*n,
                'SellValue':lambda n:0.05*n,
            }
            ss.append(section('Ranks',['Rank 0 contributes no bonus. Buying rank n costs n distilled nightmares; total cost to reach rank n from zero is n × (n + 1) / 2. The listed values feed into the system formulas described in the prestige guide.'],['Rank','Bonus / modifier','Total nightmares spent'],[[n,f'{rank_values[identifier](n)*100:g}%',n*(n+1)//2] for n in (1,2,3,5,10)]))
        rows=field_rows(f,('Description','DisplayName','Label'))
        if cat=='Challenges':
            rows.append(['Triggered',f.get('Triggered','false (default)')]);rows.append(['Trigger chance',f.get('TriggerChance','0.05f (default, applies only to triggered challenges)')])
            qs=[q for q in questdefs if re.search(r'QuestChallenge\.'+re.escape(identifier)+r'\b',q['fields'].get('Challenges',''))]
            if qs:ss.append(section('Appears on quests',headers=['Quest'],rows=[[ref('quest:'+q['id'],tr(q['id']))] for q in qs]))
        hooks=[k for k,v in f.items() if '=>' in v]
        if hooks:ss.append(section('Behavior hooks',['This definition changes '+', '.join(words(h).lower() for h in hooks)+'. The system guides explain the calculation order; the exact callback expressions are preserved below.']))
        if rows:ss.append(section('Properties',headers=['Property','Value'],rows=rows))
        add(prefix+':'+identifier,title,cat,desc or f'{title} is a {cat.lower().rstrip("s")} definition used by the game simulation.',ss,[source(path,line_at(text,m.start()))],icon=lit(f.get('IconName')),technical=f)

for path,text in files.items():
    if not path.startswith('Assets.Source.Adventure.Dungeons/'):continue
    m=re.search(r'DungeonType (\w+) = new DungeonType\("([^"]+)"\)',text)
    if not m:continue
    variable,identifier=m.groups();f={k:v for k,v in re.findall(re.escape(variable)+r'\.(\w+)\s*=\s*([^;]+);',text)}
    stdefs=[]
    for sm in re.finditer(r'new DungeonStage\("([^"]+)"\)\s*\{',text):
        st=sm.end()-1;end=block_end(text,st);sf=fields(text[st+1:end]);stageid=sm[1];stdefs.append((stageid,sf,line_at(text,sm.start())))
        ss=[];rs=field_rows(sf,('Challenges','Rewards','EnemySprites'))
        ss.append(section('Stage values',['Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.'],['Property','Base value'],rs))
        challenges=re.findall(r'QuestChallenge\.(\w+)',sf.get('Challenges',''))
        if challenges:ss.append(section('Challenges',headers=['Challenge'],rows=[[ref('challenge:'+c,words(c))] for c in challenges]))
        rs=rewards(sf.get('Rewards',''))
        if rs:ss.append(section('Rewards',headers=['Reward','Base amount','Rule'],rows=rs))
        ss.append(section('Dungeon',headers=['Dungeon'],rows=[[ref('dungeon:'+identifier,tr('dungeon_'+identifier))]]))
        add('stage:'+stageid,tr(stageid) if stageid in names else words(stageid),'Dungeon stages',f'Stage {len(stdefs)} of {tr("dungeon_"+identifier)}.',ss,[source(path,line_at(text,sm.start()))],technical=sf)
    ss=[];desc=tr(lit(f.get('Description')) or '@dungeon_'+identifier+'_desc')
    if desc:ss.append(section('Overview',[desc]))
    rs=field_rows(f,('DisplayName','Description','IsAvailable','SupplyCost'))
    if f.get('SupplyCost'):rs.append(['Supplies per run',currency_text(f['SupplyCost']) or f['SupplyCost']])
    if f.get('IsAvailable'):rs.append(['Availability condition',f['IsAvailable']])
    ss.append(section('Entry requirements',headers=['Property','Value'],rows=rs))
    ss.append(section('Stages in order',headers=['Stage','Base difficulty','Base health','Challenges'],rows=[[ref('stage:'+i,tr(i) if i in names else words(i)),sf.get('BaseDifficulty'),sf.get('BaseHealth'),', '.join(words(c) for c in re.findall(r'QuestChallenge\.(\w+)',sf.get('Challenges','')))] for i,sf,_ in stdefs]))
    add('dungeon:'+identifier,tr(lit(f.get('DisplayName')) or '@dungeon_'+identifier),'Dungeons',desc,ss,[source(path,line_at(text,m.start()))],icon=lit(f.get('IconName')),technical=f)

for r in definitions('Assets.Source.Adventure.Wars',r'new (?P<kind>WarType)\("(?P<id>[^"]+)"\)\s*\{'):
    f=r['fields'];identifier=r['id'];ss=[];stages=[]
    for sm in re.finditer(r'new WarStage\s*\{',f.get('Stages','')):
        st=sm.end()-1;end=block_end(f['Stages'],st);sf=fields(f['Stages'][st+1:end]);stages.append(sf)
    for i,sf in enumerate(stages,1):
        sr=[]
        for key in ('Description','RewardDescription','RewardComplete'):
            if lit(sf.get(key)):sr.append(section(words(key),[tr(lit(sf[key]))]))
        sr.append(section('Campaign parameters',headers=['Parameter','Amount'],rows=field_rows(sf,('DisplayName','Description','RewardDescription','RewardComplete'))))
        add('war-stage:'+identifier+':'+str(i),tr(lit(sf.get('DisplayName')) or identifier+f' stage {i}'),'War stages',f'Stage {i} of {tr(lit(f.get("DisplayName")) or identifier)}.',sr,[source(r['path'],r['line'])],icon=lit(sf.get('IconName')),technical=sf)
    if description(identifier,f):ss.append(section('Campaign',[description(identifier,f)]))
    ss.append(section('Stages',headers=['Stage','Progress','Enemy damage','Starting strength','Ending strength'],rows=[[ref('war-stage:'+identifier+':'+str(i),tr(lit(sf.get('DisplayName')) or f'Stage {i}')),sf.get('ProgressAmount'),sf.get('EnemyDamage'),sf.get('StartStrength'),sf.get('EndStrength')] for i,sf in enumerate(stages,1)]))
    add('war:'+identifier,tr(lit(f.get('DisplayName')) or identifier),'Wars',description(identifier,f),ss,[source(r['path'],r['line'])],icon=lit(f.get('IconName')),technical={k:v for k,v in f.items() if k!='Stages'})

# Reward links work in both directions: a material page identifies its adventure sources.
for a in list(articles):
    if a['category'] not in ('Quests','Dungeon stages'):continue
    for sec in a['sections']:
        if 'reward' not in sec['title'].lower() or not sec.get('table'):continue
        for row in sec['table']['rows']:
            target=row[0] if row else None
            if not isinstance(target,dict) or not target.get('id','').startswith('item:') or target['id'] not in byid:continue
            dest=byid[target['id']]
            found=next((s for s in dest['sections'] if s['title']=='Adventure sources'),None)
            if not found:
                found=section('Adventure sources',headers=['Source','Reward set','Base amount / rule'],rows=[])
                found['table']={'headers':['Source','Reward set','Base amount / rule'],'rows':[]}
                dest['sections'].append(found)
            found['table']['rows'].append([ref(a['id'],a['title']),sec['title'],' · '.join(str(x) for x in row[1:])])

currency_values={'Gold':1,'Requisition':1000,'Medal':600,'Ring':1200,'Mana':11,'Crown':2400,'Ducat':5200,'Ingenuity':200,'Faith':100}
currency_icons={'Gold':'Icons_8','Requisition':'Icons_33','Medal':'Icons_63','Ring':'Icons_135','Mana':'Icons_162','Crown':'Icons_188','Ducat':'Icons_197','Ingenuity':'Icons2_67','Faith':'Icons2_66'}
currency_unlocks={'Gold':None,'Requisition':'requisition_office','Medal':'war_effort','Ring':'quest_board','Mana':'enchanter','Crown':'restaurant','Ducat':'dungeon','Ingenuity':'inventor','Faith':'shrine'}
for key,value in currency_values.items():
    desc=clean(names.get('Currency'+key+'Desc',''))
    ss=[section('In the game',[desc]),section('Reference',headers=['Property','Value'],rows=[['Internal currency',key],['Base coin equivalent per unit',value],['Tradeable on exchange','No' if key in ('Mana','Ingenuity','Faith') else 'Yes'],['Visibility unlock',ref('tech:'+currency_unlocks[key],tr(currency_unlocks[key])) if currency_unlocks[key] else 'Always']])]
    if key=='Gold':ss.append(section('Coin denominations',['Code stores the Gold currency in its smallest coin unit. 100 base units = 1 silver; 10,000 base units = 1 displayed gold. The raw amount 1,950 is 19 silver and 50 copper, not 1,950 displayed gold.']))
    add('currency:'+key,tr('Currency'+key),'Currencies',desc.split('\n')[0],ss,[source('Assets.Source.Player/CurrencyExtensions.cs',1),source('Assets.Behaviour.UI.Shared/CurrencyDisplay.cs',1)],icon=currency_icons[key])

# Upgrade classes, enum members, and Steam achievement triggers fill out the reference.
for path,text in files.items():
    if not path.startswith('Assets.Source.Flow.Upgrades/'):continue
    kind=Path(path).stem
    prop={k:v for k,v in re.findall(r'\b(\w+)\s*=>\s*"([^"\n]*)";',text)}
    constants=re.findall(r'public const [\w]+ (\w+)\s*=\s*([^;]+)',text)
    ss=[]
    if constants:ss.append(section('Constants',headers=['Value','Amount'],rows=[[words(k),v] for k,v in constants]))
    effects=[words(x) for x in re.findall(r'public override [\w<>]+ (Get\w+|IsAvailableFor)\(',text)]
    if effects:ss.append(section('Changes to the building',[', '.join(effects)+'. See production and upgrade guides for how these changes combine.']))
    for key in (kind.lower()+'_desc',kind+'_desc'):
        if key in names:ss.insert(0,section('Effect',[clean(names[key])]))
    add('upgrade:'+kind,tr(prop.get('DisplayName',kind)),'Upgrades',f'{tr(prop.get("DisplayName",kind))} is a building add-on.',ss,[source(path,1)],icon=prop.get('IconName'))

for path,text in files.items():
    if '/LightJson' in '/'+path or path.startswith('Properties/'):continue
    for m in re.finditer(r'public enum (\w+)\s*\{',text):
        st=m.end()-1;end=block_end(text,st);members=split_top(text[st+1:end]);kind=m[1]
        rows=[]
        for i,entry in enumerate(members):
            key=entry.split('=')[0].strip()
            if not re.fullmatch(r'\w+',key):continue
            rows.append([words(key),entry.strip()])
        add('enum:'+kind,words(kind),'Glossary',f'All {len(rows)} values declared for {words(kind).lower()}.',[section('Values',headers=['Name','Code value'],rows=rows)],[source(path,line_at(text,m.start()))])

achievement_sources=defaultdict(list)
for path,text in files.items():
    for m in re.finditer(r'SteamAchievement.Trigger\("([^"]+)"\)',text):achievement_sources[m[1]].append(source(path,line_at(text,m.start())))
for key,ss in achievement_sources.items():
    excerpt=[]
    for so in ss:
        lines=files[so['path']].splitlines();start=max(0,so['line']-7);end=min(len(lines),so['line']+2)
        excerpt.append(section('Trigger context: '+Path(so['path']).stem,code='\n'.join(f'{i+1:>4}  {lines[i]}' for i in range(start,end))))
    add('achievement:'+key,words(key),'Achievements',f'Steam achievement trigger {key}. The nearby conditions below identify when the game calls it.',excerpt,ss)

# Human-authored research is integrated after deterministic entity extraction.
research_count=0
for p in sorted((ROOT/'research').glob('*.json')):
    data=json.loads(p.read_text(encoding='utf-8-sig'))
    if isinstance(data,dict):data=data.get('articles',data.get('pages',[]))
    for a in data:
        if a['id'] in byid:a['id']='guide:'+a['id']
        a.setdefault('category','Guides')
        if p.stem=='interface':a['category']='Interface'
        add(a['id'],a['title'],a['category'],a.get('summary',''),a.get('sections',[]),a.get('sources',[]),kind='guide')
        research_count+=1

# Connect each reference to relevant explanatory guides by shared implementation files.
guides=[a for a in articles if a.get('kind')=='guide']
for a in articles:
    aset={s['path'] for s in a['sources']}
    matches=sorted(((len(aset&{s['path'] for s in g['sources']}),g) for g in guides if g['id']!=a['id']),key=lambda x:-x[0])
    a['related']=[ref(g['id'],g['title']) for n,g in matches[:6] if n>0]
    if a.get('icon') in icons:a['iconUrl']=icons[a['icon']]

# Each game source file is indexed, including third-party infrastructure with explicit classification.
inventory=[]
for path,text in files.items():
    lines=text.splitlines();third=path.startswith(('LightJson/','LightJson.Serialization/','Properties/')) or Path(path).stem=='SteamManager'
    symbols=[]
    for i,line in enumerate(lines,1):
        if re.match(r'\s*(?:public|protected|internal)\s+',line) and len(line.strip())<260:
            symbols.append([i,line.strip().rstrip(';')])
    references=sorted(coverage[path]);fileid='source:'+path
    sections=[section('Audit classification',[('Bundled infrastructure / metadata.' if third else 'Game implementation, UI, data definition or utility.')+' Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.']),section('Public and protected symbols',headers=['Line','Declaration'],rows=symbols)]
    if references:sections.append(section('Documented by',headers=['Wiki article'],rows=[[ref(x,byid[x]['title'])] for x in references]))
    if not references and not third:sections.append(section('Coverage note',['This file has a complete symbol inventory but no dedicated explanatory guide citation. Its implementation remains available in the local source folder. This is an explicit documentation gap, not a claim that every behavior has been manually explained.']))
    add(fileid,Path(path).stem+' — source reference','Source audit',f'{path} · {len(lines):,} lines · '+('infrastructure' if third else f'{len(references)} linked articles'),sections,[source(path,1)],kind='source')
    inventory.append({'path':path,'lines':len(lines),'sha256':hashlib.sha256(text.encode()).hexdigest(),'infrastructure':third,'articles':references,'symbols':len(symbols)})

hashvalue=hashlib.sha256((GAME/'KingdomInc_Data'/'Managed'/'Assembly-CSharp.dll').read_bytes()).hexdigest()
unexplained=[x['path'] for x in inventory if not x['infrastructure'] and not x['articles']]
counts=dict(Counter(a['category'] for a in articles))
meta={'title':'Kingdom Inc Wiki','date':'2026-11-03','assemblySha256':hashvalue,'sourceFiles':len(files),'sourceLines':sum(x['lines'] for x in inventory),'articles':len(articles),'guideArticles':research_count,'categories':counts,'uncitedFiles':unexplained,'localizationEntries':len(names),'sourceRoot':str(SRC),'extraction':'Fresh ILSpy decompilation of the installed Assembly-CSharp.dll; current resources.assets English localization. No game assembly executed.','limitations':['Static inspection does not validate Unity prefab settings, runtime mod patches or actual gameplay results.','Some definition fields are callbacks or dynamic expressions. They remain labeled in implementation details rather than being evaluated or assigned invented values.','Developer-only or hidden definitions are included and labeled where established by code. Presence in the assembly does not prove normal-game availability.','Icons use the existing local sprite export; mechanics and English text use the freshly inspected build.','Every source file is inventoried. Files without explanatory citations are listed explicitly in the audit.']}
save(DATA/'coverage.json',{'metadata':meta,'files':inventory})

add('coverage','Coverage and provenance','Reference','The exact build, extraction scope, documentation coverage and verification limits.',[
    section('Installed build',headers=['Property','Value'],rows=[['Inspected on','November 3, 2026'],['Assembly SHA-256',hashvalue],['C# files',len(files)],['Lines of code',meta['sourceLines']],['Mechanics guides',research_count],['Localization entries',len(names)]]),
    section('How to read this wiki',['Mechanics guides explain the gameplay rules. Individual reference pages list definition values and relationships. Source audit pages inventory every file and link back to its documented topics. Implementation details retain complex expressions for traceability. Base values should not be treated as final throughput or live combat performance.']),
    section('Limits and unresolved work',meta['limitations']),
    section('Files without explanatory citations',['These files are inventoried, but no explanatory article currently cites them. UI and support files often appear here; inspect their source reference before assuming coverage is complete.'],['Source file'],[[ref('source:'+x,x)] for x in unexplained]),
],[],kind='guide')

add('home','The kingdom, documented.','Reference','A searchable field guide to production, progression and adventure, derived from the installed game code.',[
    section('Start here',['Build resource supply, turn materials into higher-value goods, sell them to fund research, and use war and adventure rewards to open the next production tier. This wiki connects each item to its recipes, research and uses so you can follow a whole chain.']),
    section('Reference collections',headers=['Collection','Entries'],rows=[[cat,n] for cat,n in counts.items() if cat!='Source audit']),
    section('Code you can trace',[f'The reference was generated from {len(files)} freshly decompiled C# files ({meta["sourceLines"]:,} lines). It includes direct definitions and helper-generated research nodes, plus explanatory mechanics guides. See Coverage and provenance for the assembly hash, coverage gaps and runtime limits.']),
],[],kind='guide')

# Validate citations and cross references, and repair only explicitly optional relationship links.
broken=[]
def walk(obj):
    if isinstance(obj,dict):
        if 'id' in obj and 'label' in obj and len(obj)<=2 and obj['id'] not in byid:broken.append(obj)
        for v in obj.values():walk(v)
    elif isinstance(obj,list):
        for v in obj:walk(v)
for a in articles:
    for so in a['sources']:
        assert so['path'] in files,f'Unknown citation {so} in {a["id"]}'
        assert 1<=so['line']<=len(files[so['path']].splitlines()),f'Bad citation {so}'
    walk(a)
if broken:
    # Category pages sometimes link a recipe station alias; unresolved links are rendered as text and reported.
    print('Unresolved reference targets:',dict(Counter(x['id'] for x in broken)))
    for b in broken:b['unresolved']=True

meta['articles']=len(articles);meta['categories']=dict(Counter(a['category'] for a in articles));meta['brokenReferences']=len(broken)
payload={'meta':meta,'articles':articles}
save(DIST/'wiki-data.json',payload)
(DIST/'wiki-data.js').write_text('window.WIKI_DATA = '+json.dumps(payload,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')

# Standalone Markdown export is portable to a conventional wiki engine.
MD=ROOT/'markdown';MD.mkdir(exist_ok=True)
def mdname(identifier):return re.sub(r'[^a-zA-Z0-9_.-]+','-',identifier)+'.md'
def mdvalue(v):
    if isinstance(v,dict) and 'label' in v:return '['+str(v['label'])+']('+mdname(v['id'])+')' if v['id'] in byid else str(v['label'])
    return str(v if v is not None else '').replace('|','\\|').replace('\n',' ')
for a in articles:
    out=['# '+a['title'],'',a['summary'],'']
    for s in a['sections']:
        out+=['## '+s['title'],'']
        for p in s.get('paragraphs',[]):out += [str(p),'']
        if s.get('table'):
            t=s['table'];out+=['| '+' | '.join(t['headers'])+' |','| '+' | '.join(['---']*len(t['headers']))+' |']
            out+=['| '+' | '.join(mdvalue(v) for v in row)+' |' for row in t['rows']];out+=['']
        if s.get('code'):out+=['```csharp',s['code'],'```','']
    if a.get('technical'):out+=['<details><summary>Implementation fields</summary>','','```json',json.dumps(a['technical'],indent=2,ensure_ascii=False),'```','','</details>','']
    if a['sources']:out+=['## Sources','']+[f'- `{s["path"]}:{s["line"]}`' for s in a['sources']]
    (MD/mdname(a['id'])).write_text('\n'.join(out)+'\n',encoding='utf-8')
(MD/'README.md').write_text('# Kingdom Inc Wiki\n\n[Open the wiki](home.md) · [Coverage](coverage.md)\n\n'+ '\n'.join(f'- [{a["title"]}]({mdname(a["id"])})' for a in articles if a.get('kind')=='guide')+'\n',encoding='utf-8')
save(ROOT/'validation.json',{'assemblySha256':hashvalue,'sourceFiles':len(files),'pages':len(articles),'mechanicsGuides':research_count,'categories':meta['categories'],'validCitations':sum(len(a['sources']) for a in articles),'unresolvedReferences':len(broken),'unexplainedSourceFiles':unexplained})
print(json.dumps({'pages':len(articles),'guides':research_count,'categories':meta['categories'],'unresolvedReferences':len(broken),'uncitedFiles':len(unexplained)},indent=2))

