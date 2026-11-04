# Kingdom Inc Wiki

Open [the offline wiki](dist/index.html) in a browser. It works directly from disk; its fonts, artwork, code, and data are local. [The Markdown edition](markdown/README.md) contains a separate file for each article and source reference.

The wiki documents the installed November 3, 2026 build, freshly decompiled with ILSpy. The assembly SHA-256 is recorded in `source-manifest.json` and the wiki's Coverage and provenance page. Original game binaries and saves were not modified.

## Content

The wiki contains explanatory mechanics and interface guides plus individual references for items, characters, recipes, research, buildings, enhancements, upgrades, currencies, quests, dungeons, dungeon stages, wars, war stages, traits, challenges, prestige perks, achievements, and enums. Every C# source file is inventoried and linked to the relevant documentation. Complex C# fields remain visible in expandable implementation details.

Search covers article titles, descriptions and tables. Source audit results can be included with the search checkbox. Articles support bookmarks, link copying, printing and Markdown export. Bookmarks stay in the browser.

## Rebuilding this inspected version

Run these commands from the game directory:

```powershell
python Wiki/tools/index_calculator_data.py
python Wiki/tools/build_wiki.py
python Wiki/tools/validate_wiki.py
node --check Wiki/dist/app.js
```

The local, ignored `source/` folder and `data/localization.json` are required for a rebuild. The build refuses to run if the installed assembly's hash has changed. After a game update, first create a new decompilation and English resource extraction, update the source manifest, and review the explanatory guides against the changed implementation. Do not just update the hash to bypass that review.

## Verification boundaries

This is static documentation. Unity prefab settings, mods that patch behavior, and actual runtime results can differ. Source references, coverage and limitations are visible in the wiki. The Source audit collection distinguishes game code and bundled infrastructure.

The visual theme uses the game's locally extracted logo, icons, factory grid, room art and fonts. Game artwork and third-party fonts remain credited to their respective creators. This is an independent reference.
