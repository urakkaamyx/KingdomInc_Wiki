'use strict';
(() => {
const data=window.WIKI_DATA;
if(!data){document.querySelector('main').textContent='Wiki data could not be loaded. Keep wiki-data.js beside index.html.';return;}
const pages=new Map(data.articles.map(a=>[a.id,a]));
const groups=[
  ['THE FIELD GUIDE',[['Overview','⌂','home'],['Mechanics guides','✧','guides'],['Progression','↟','Progression'],['Production','⚒','Production'],['Adventure','⚔','Adventure']]],
  ['THE ENCYCLOPEDIA',[['Items','◇','Items'],['Recipes','⚒','Recipes'],['Buildings','♜','Buildings'],['Research','⌘','Research'],['Classes','♞','Classes'],['Enhancements','✧','Enhancements'],['Upgrades','↑','Upgrades']]],
  ['BEYOND THE FACTORY',[['Quests','⚑','Quests'],['Dungeons','▱','Dungeons'],['Dungeon stages','↳','Dungeon stages'],['Wars','⚔','Wars'],['War stages','↳','War stages'],['Traits','✶','Traits'],['Challenges','◈','Challenges'],['Prestige','♛','Prestige'],['Achievements','✵','Achievements']]],
  ['THE ARCHIVE',[['Currencies','◉','Currencies'],['Interface','▣','Interface'],['Reference','≡','Reference'],['Glossary','Aa','Glossary'],['Source audit','⌗','Source audit']]]
];
let saved;try{saved=new Set(JSON.parse(localStorage.getItem('kingdom-wiki:saved')||'[]'));}catch{saved=new Set();}
const main=document.querySelector('main'),search=document.querySelector('#search'),nav=document.querySelector('#nav');
const esc=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const url=id=>'#page/'+encodeURIComponent(id);
const caturl=cat=>'#category/'+encodeURIComponent(cat);
const count=cat=>cat==='guides'?data.articles.filter(a=>a.kind==='guide'&&a.id!=='home'&&a.id!=='coverage').length:data.articles.filter(a=>a.category===cat).length;
const plain=v=>typeof v==='object'&&v?String(v.label||JSON.stringify(v)):String(v??'');
const val=v=>v&&typeof v==='object'&&'label'in v?(pages.has(v.id)?`<a href="${url(v.id)}">${esc(v.label)}</a>`:esc(v.label)):esc(v);
function countSaved(){document.querySelector('#saved-count').textContent=saved.size;}
countSaved();
nav.innerHTML=groups.map(([title,entries])=>`<div class="nav-heading">${title}</div>${entries.map(([label,icon,cat])=>`<a class="nav-item" data-nav="${esc(cat)}" href="${cat==='home'?url('home'):caturl(cat)}"><span class="nav-icon" aria-hidden="true">${icon}</span>${label}<span class="nav-count">${cat==='home'?'':count(cat).toLocaleString()}</span></a>`).join('')}`).join('');
document.querySelector('#footer-count').textContent=`${data.meta.sourceFiles} source files · ${data.meta.articles.toLocaleString()} articles`;
const sourceIds=new Set(data.articles.filter(a=>a.kind==='source').map(a=>a.id));
const index=data.articles.map(a=>({a,title:(a.title+' '+a.id).toLowerCase(),text:(a.summary+' '+a.sections.map(s=>s.title+' '+(s.paragraphs||[]).join(' ')+' '+(s.table?s.table.rows.map(r=>r.map(plain).join(' ')).join(' '):'')).join(' ')).toLowerCase()}));
function breadcrumb(cat,title){document.querySelector('#breadcrumb').innerHTML=`THE CODEX <span>/</span> ${esc(cat)}${title?' <span>/</span> '+esc(title):''}`;}
function active(cat){document.querySelectorAll('[data-nav]').forEach(n=>n.classList.toggle('active',n.dataset.nav===cat));}
function sectionHtml(s,i){return `<section id="section-${i}" class="article-section"><h2>${esc(s.title)}</h2>${(s.paragraphs||[]).map(p=>`<p>${esc(p)}</p>`).join('')}${s.table?`<div class="table-wrap"><table><thead><tr>${s.table.headers.map(h=>`<th scope="col">${esc(h)}</th>`).join('')}</tr></thead><tbody>${s.table.rows.map(r=>`<tr>${r.map(v=>`<td>${val(v)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`:''}${s.code?`<pre><code>${esc(s.code)}</code></pre>`:''}</section>`;}
function article(a){
 breadcrumb(a.category,a.title);active(a.id==='home'?'home':a.category);document.title=a.title+' · Kingdom Inc Wiki';
 main.innerHTML=`<div class="eyebrow"><span class="status-dot"></span>${esc(a.category)} <span>·</span> CODE REFERENCE</div><div class="article-top"><div class="article-title">${a.iconUrl?`<img src="${esc(a.iconUrl)}" alt="">`:''}<h1>${esc(a.title)}</h1></div><div class="article-actions"><button id="save-page" class="${saved.has(a.id)?'saved':''}" aria-pressed="${saved.has(a.id)}">${saved.has(a.id)?'★ Saved':'☆ Save'}</button><button id="download-page">Export .md</button><button id="copy-page">Copy link</button></div></div><p class="article-summary">${esc(a.summary)}</p><div class="article-grid"><div class="article-body">${a.sections.map(sectionHtml).join('')}${a.technical?`<details><summary>Implementation details · exact definition fields</summary><p class="note">These are static C# expressions. Conditional callbacks and inherited behavior are preserved rather than evaluated into invented fixed values.</p>${Object.entries(a.technical).map(([k,v])=>`<div class="field"><h3>${esc(k)}</h3><pre><code>${esc(v)}</code></pre></div>`).join('')}</details>`:''}${a.sources.length?`<div class="sources"><h3>SOURCE EVIDENCE</h3><p>Fresh decompilation · installed assembly ${esc(data.meta.assemblySha256.slice(0,16))}…</p><ul>${a.sources.map(s=>`<li><a href="${url('source:'+s.path)}">${esc(s.path)}</a> : line ${s.line}</li>`).join('')}</ul><p>Static inspection. <a href="${url('coverage')}">Build, coverage and runtime limits ↗</a></p></div>`:''}${a.related?.length?`<div class="related"><h3>Read alongside</h3><div class="related-links">${a.related.map(r=>`<a href="${url(r.id)}">${esc(r.label)} ↗</a>`).join('')}</div></div>`:''}</div><nav class="toc" aria-label="On this page"><strong>ON THIS PAGE</strong>${a.sections.map((s,i)=>`<a href="#section-${i}" data-section="${i}">${esc(s.title)}</a>`).join('')}</nav></div>`;
 document.querySelectorAll('[data-section]').forEach(n=>n.onclick=e=>{e.preventDefault();document.querySelector('#section-'+n.dataset.section)?.scrollIntoView({behavior:'smooth'});});
 document.querySelector('#save-page').onclick=()=>{if(saved.has(a.id))saved.delete(a.id);else saved.add(a.id);try{localStorage.setItem('kingdom-wiki:saved',JSON.stringify([...saved]));}catch{}countSaved();let b=document.querySelector('#save-page');b.classList.toggle('saved',saved.has(a.id));b.textContent=saved.has(a.id)?'★ Saved':'☆ Save';b.setAttribute('aria-pressed',saved.has(a.id));};
 document.querySelector('#download-page').onclick=()=>download(a);
 document.querySelector('#copy-page').onclick=async()=>{try{await navigator.clipboard.writeText(location.href);toast('Article link copied');}catch{toast('Copy the article URL from the address bar');}};
}
function cards(list){return list.map(a=>`<a class="result" href="${url(a.id)}">${a.iconUrl?`<img src="${esc(a.iconUrl)}" alt="" loading="lazy">`:''}<div class="result-body"><div class="result-category">${esc(a.category)}</div><h3>${esc(a.title)}</h3><p>${esc(a.summary)}</p></div></a>`).join('');}
function listPage(title,summary,list,category){
 breadcrumb(category||title);active(category||'');document.title=title+' · Kingdom Inc Wiki';
 let visible=80;
 main.innerHTML=`<div class="eyebrow"><span class="status-dot"></span>THE ENCYCLOPEDIA</div><div class="category-heading"><div><h1>${esc(title)}</h1><p>${esc(summary)}</p></div><span class="badge">${list.length.toLocaleString()} entries</span></div><div class="result-controls"><span id="shown-count"></span><label>Sort <select id="sort"><option value="name">Name A–Z</option><option value="category">Category</option></select></label></div><div class="result-list" id="results"></div><button class="button load-more" id="more">Show more entries ↓</button>`;
 const render=()=>{document.querySelector('#results').innerHTML=list.length?cards(list.slice(0,visible)):'<div class="empty">No articles match this view.</div>';document.querySelector('#shown-count').textContent=`Showing ${Math.min(visible,list.length).toLocaleString()} of ${list.length.toLocaleString()}`;document.querySelector('#more').hidden=visible>=list.length;};
 document.querySelector('#more').onclick=()=>{visible+=80;render();};
 document.querySelector('#sort').onchange=e=>{list.sort((a,b)=>e.target.value==='category'?a.category.localeCompare(b.category)||a.title.localeCompare(b.title):a.title.localeCompare(b.title));render();};
 render();
}
function category(cat){const list=data.articles.filter(a=>cat==='guides'?a.kind==='guide'&&!['home','coverage'].includes(a.id):a.category===cat).sort((a,b)=>a.title.localeCompare(b.title));listPage(cat==='guides'?'Mechanics guides':cat,cat==='Source audit'?'Every decompiled C# file, with symbols, source hashes and links to documented behavior.':'Browse the installed game’s definitions and the rules behind them.',list,cat);}
function home(){
 active('home');breadcrumb('Overview');document.title='Kingdom Inc Wiki · The Codex';
 const firstGuide=term=>data.articles.find(a=>a.kind==='guide'&&term.test(a.title))?.id||'coverage';
 const collections=[['Items','◇','Materials, equipment, supplies, and the people who keep the kingdom moving.'],['Recipes','⚒','Ingredients, outputs, stations, currency costs, and special transformations.'],['Buildings','♜','The complete factory. Gathering, crafting, routing, storage, and services.'],['Research','⌘','Follow prerequisites, tier gates, and everything a discovery unlocks.'],['Classes','♞','Base stats, class traits, equipment requirements, and advancement paths.'],['Dungeons','▱','Every dungeon and stage, with challenges, entry requirements, and rewards.']];
 main.innerHTML=`<div class="hero"><div><div class="eyebrow"><span class="status-dot"></span>THE KINGDOM INC FIELD GUIDE</div><h1>The kingdom,<br><em>documented.</em></h1><p class="intro">From the first iron ingot to the last nightmare. Explore the systems, follow the production chains, and find the numbers behind your kingdom.</p><div class="hero-links"><a class="button primary" href="${caturl('guides')}">Explore the guides <span>↗</span></a><a class="button" href="${url('coverage')}">How this wiki was built</a></div></div><div class="hero-art" aria-hidden="true"><img class="game-logo" src="assets/game/KingdomIncLogo_3x.png" alt=""><span class="hero-tag">BUILD. CRAFT. CONQUER.</span></div></div><div class="stats"><div class="stat"><strong>${(count('Items')+count('Classes')).toLocaleString()}</strong><span>Items &amp; characters</span></div><div class="stat"><strong>${count('Recipes')}</strong><span>Crafting recipes</span></div><div class="stat"><strong>${count('Research')}</strong><span>Research nodes</span></div><div class="stat"><strong>${data.meta.sourceFiles}</strong><span>Source files indexed</span></div></div><div class="factory-strip" aria-label="A Kingdom Inc production chain"><div class="factory-room"><span>Mine</span><img src="assets/game/Mine.png" alt="Mine building"></div><span class="factory-pipe" aria-hidden="true"></span><div class="factory-room"><span>Forge</span><img src="assets/game/Forge.png" alt="Forge building"></div><span class="factory-pipe" aria-hidden="true"></span><div class="factory-room"><span>Blacksmith</span><img src="assets/game/Blacksmith.png" alt="Blacksmith building"></div></div><div class="section-header"><h2>Explore the encyclopedia</h2><span>FOLLOW YOUR CURIOSITY</span></div><div class="collections">${collections.map(([c,icon,description])=>`<a class="collection" href="${caturl(c)}"><div class="collection-top"><span class="collection-symbol" aria-hidden="true">${icon}</span><span class="collection-number">${count(c)} ENTRIES</span></div><h3>${c==='Items'?'Items & resources':c==='Research'?'Research & unlocks':c==='Classes'?'Adventurers & classes':c==='Dungeons'?'Dungeons & rewards':c}</h3><p>${description}</p><div class="collection-bottom"><span>Open collection</span><span>↗</span></div></a>`).join('')}</div><div class="guide-shelf"><div class="feature"><div class="eyebrow">UNDERSTAND THE SYSTEMS</div><h3>A little knowledge.<br>A better kingdom.</h3><p>Read the mechanics guides for the formulas, timing rules, and interactions that a stat table cannot explain.</p><ul>${[[firstGuide(/flow|simulation|routing/i),'How your factory moves'],[firstGuide(/armor|damage|combat/i),'Inside the combat calculations'],[firstGuide(/prestige|ascension/i),'Building toward the next ascension']].map(([id,label])=>`<li><a href="${url(id)}">${label}<span>↗</span></a></li>`).join('')}</ul></div><div><div class="eyebrow">THE SMALL PRINT, MADE VISIBLE</div><h2>Every number has a source.</h2><p class="intro">Built from ${data.meta.sourceLines.toLocaleString()} lines of freshly decompiled game code. Reference pages link to their implementation file and line; the source audit records the full inspection scope.</p><p class="note">Definition values describe the inspected base game. Mod patches, dynamic multipliers, prefab settings, and runtime behavior can affect the result. Coverage gaps are listed in the audit.</p><a class="button" href="${url('coverage')}">See coverage &amp; provenance <span>↗</span></a></div></div>`;
}
function doSearch(query,includeSources=false){
 const tokens=query.trim().toLowerCase().split(/\s+/).filter(Boolean);
 const hits=index.filter(({a,title,text})=>(includeSources||a.kind!=='source')&&tokens.every(t=>title.includes(t)||text.includes(t))).map(({a,title})=>({a,score:tokens.reduce((n,t)=>n+(title===t?20:title.startsWith(t)?8:title.includes(t)?4:0),0)+(a.kind==='guide'?1:0)})).sort((a,b)=>b.score-a.score||a.a.title.localeCompare(b.a.title)).map(h=>h.a);
 listPage('Search results',`Results for “${query}” across titles, descriptions, formulas, and reference tables.`,hits,'Search');
 const controls=document.querySelector('.result-controls');const label=document.createElement('label');label.innerHTML=`<input type="checkbox" id="include-source" ${includeSources?'checked':''}> Include source audit`;controls.prepend(label);document.querySelector('#include-source').onchange=e=>doSearch(query,e.target.checked);
}
let timer;search.oninput=()=>{clearTimeout(timer);timer=setTimeout(()=>{if(search.value.trim())doSearch(search.value);else route();},120);};
search.onkeydown=e=>{if(e.key==='Escape'){search.value='';search.blur();route();}if(e.key==='Enter'){const q=search.value.trim();if(q)location.hash='#search/'+encodeURIComponent(q);}};
document.querySelector('#search-focus').onclick=()=>search.focus();
document.querySelector('#print').onclick=()=>print();
document.querySelector('#menu').onclick=()=>{let open=document.querySelector('#sidebar').classList.toggle('open');document.querySelector('#menu').setAttribute('aria-expanded',open);};
document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)){e.preventDefault();search.focus();}if(e.key==='Escape'){document.querySelector('#sidebar').classList.remove('open');document.querySelector('#menu').setAttribute('aria-expanded','false');}});
document.addEventListener('click',e=>{const a=e.target.closest('a');if(a?.classList.contains('skip')){e.preventDefault();main.focus();return;}if(a&&a.getAttribute('href')?.startsWith('#')&&!a.dataset.section){search.value='';document.querySelector('#sidebar').classList.remove('open');document.querySelector('#menu').setAttribute('aria-expanded','false');}});
function route(){
 const raw=location.hash.slice(1)||'page/home';let arg;try{arg=decodeURIComponent(raw.slice(raw.indexOf('/')+1));}catch{arg='home';}
 if(raw.startsWith('page/')){const a=pages.get(arg);if(a){if(arg==='home')home();else article(a);}else listPage('Article not found','Try searching for a title or browsing a collection.',[],'Reference');}
 else if(raw.startsWith('category/'))category(arg);
 else if(raw==='bookmarks')listPage('Saved articles','Your reading list is saved in this browser.',[...saved].map(id=>pages.get(id)).filter(Boolean),'Saved');
 else if(raw.startsWith('search/')){search.value=arg;doSearch(arg);}
 else home();
 window.scrollTo(0,0);
}
window.addEventListener('hashchange',route);
function toast(message){const t=document.querySelector('#toast');t.textContent=message;t.style.display='block';setTimeout(()=>{t.style.display='none';},2400);}
function download(a){
 let lines=['# '+a.title,'',a.summary,''];
 const cell=v=>plain(v).replace(/\|/g,'\\|').replace(/\n/g,' ');
 for(const s of a.sections){lines.push('## '+s.title,'',...(s.paragraphs||[]).flatMap(p=>[p,'']));if(s.table)lines.push('| '+s.table.headers.join(' | ')+' |','| '+s.table.headers.map(()=>'---').join(' | ')+' |',...s.table.rows.map(r=>'| '+r.map(cell).join(' | ')+' |'),'');if(s.code)lines.push('```csharp',s.code,'```','');}
 if(a.sources.length)lines.push('## Sources','',...a.sources.map(s=>'- '+s.path+':'+s.line));
 const blob=new Blob([lines.join('\n')],{type:'text/markdown;charset=utf-8'}),u=URL.createObjectURL(blob),link=document.createElement('a');link.href=u;link.download=a.id.replace(/[^a-zA-Z0-9_-]/g,'-')+'.md';link.click();setTimeout(()=>URL.revokeObjectURL(u),5000);
}
route();
})();
