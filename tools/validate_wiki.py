"""Validate source coverage, citations, entity completeness, and portable wiki assets."""
from pathlib import Path
import json, re, hashlib
from collections import Counter

root=Path(__file__).resolve().parents[1]
payload=json.loads((root/'dist/wiki-data.json').read_text(encoding='utf-8'))
pages=payload['articles'];byid={p['id']:p for p in pages}
assert len(byid)==len(pages),'Duplicate page IDs'
files={p.relative_to(root/'source').as_posix():p.read_text(encoding='utf-8-sig') for p in (root/'source').rglob('*.cs')}
assert len(files)==payload['meta']['sourceFiles']
assert payload['meta']['assemblySha256']==hashlib.sha256((root.parent/'KingdomInc_Data/Managed/Assembly-CSharp.dll').read_bytes()).hexdigest()
assert not payload['meta']['uncitedFiles'],'Unexplained source files remain'
assert not payload['meta']['brokenReferences'],'Unresolved article links'
citations=0;references=0;tables=0
def visit(x):
    global references
    if isinstance(x,dict):
        if 'id' in x and 'label' in x:
            assert x['id'] in byid,x
            references+=1
        for v in x.values():visit(v)
    elif isinstance(x,list):
        for v in x:visit(v)
for page in pages:
    assert page['title'].strip() and page['category'].strip()
    assert isinstance(page['summary'],str)
    for s in page['sections']:
        assert s['title'].strip()
        if s.get('table'):
            t=s['table'];tables+=1
            assert all(len(row)==len(t['headers']) for row in t['rows']),(page['id'],s['title'],'Bad table width')
    for s in page['sources']:
        assert s['path'] in files,(page['id'],s)
        assert 1<=s['line']<=len(files[s['path']].splitlines()),(page['id'],s)
        citations+=1
    if page.get('iconUrl'):assert (root/'dist'/page['iconUrl']).is_file()
    visit(page)
    filename=re.sub(r'[^a-zA-Z0-9_.-]+','-',page['id'])+'.md'
    assert (root/'markdown'/filename).is_file(),filename
patterns=[('item:',r'ItemType\.Add\(new \w+\("([^"\n]+)"\)\s*\{','Assets.Source.Items.Impl/'),
          ('recipe:',r'CraftingRecipe\.Add\(new CraftingRecipe\("([^"\n]+)"\)\s*\{','Assets.Source.Items.Recipes/'),
          ('enhancement:',r'ItemEnhancement\.Add\(new ItemEnhancement\("([^"\n]+)"\)\s*\{','Assets.Source.Items.Enhancements/'),
          ('tech:',r'new TechNode\("([^"\n]+)"\)\s*\{','Assets.Source.Player.Tech/')]
entitycounts={}
for prefix,pattern,folder in patterns:
    found=[i for p,text in files.items() if p.startswith(folder) for i in re.findall(pattern,text)]
    missing=[i for i in found if prefix+i not in byid]
    assert not missing,(prefix,missing)
    entitycounts[prefix]=len(found)
for p in files:assert 'source:'+p in byid,p
for asset in ['index.html','app.js','styles.css','theme.css','assets/fonts/pixel.ttf','assets/fonts/body.ttf','assets/game/KingdomIncLogo.png','assets/game/BackgroundGrid16.png']:
    assert (root/'dist'/asset).is_file(),asset
html=(root/'dist/index.html').read_text(encoding='utf-8')
for asset in re.findall(r'(?:src|href)="([^"#]+)"',html):
    if not asset.startswith(('https:','http:')):assert (root/'dist'/asset).is_file(),asset
result={'status':'passed','pages':len(pages),'guides':payload['meta']['guideArticles'],'sourceFiles':len(files),'sourceLines':sum(len(t.splitlines()) for t in files.values()),'sourceCitations':citations,'internalLinks':references,'tables':tables,'directDefinitionCounts':entitycounts,'unexplainedSourceFiles':0,'assemblySha256':payload['meta']['assemblySha256'],'notes':['Browser interaction checks are recorded separately.','Static coverage and valid references do not imply a live gameplay test.']}
(root/'validation-complete.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
