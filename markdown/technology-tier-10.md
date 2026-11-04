# Technology tier 10: Invention and writing

Inventor follows Yensburg war research and requires Yensburg war stage 1. It grants tinker and has Ingenuity-based cost overrides. Scribe follows Inventor and grants blank_vellum and blank_tome. Advanced transformations depend on Catacombs research. Currency exchange is declared on Inventor.

## Branch overview

Inventor follows Yensburg war research and requires Yensburg war stage 1. It grants tinker and has Ingenuity-based cost overrides. Scribe follows Inventor and grants blank_vellum and blank_tome. Advanced transformations depend on Catacombs research. Currency exchange is declared on Inventor.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Inventor branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inventor | FlowElement | ; Previous war_effort_yensburg | — | yensburg war stage 1 | CostTier=10 | tinker | T10Inventor.cs:10 |
| tinker | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Inventor.cs:30 |
| widget | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Inventor.cs:38 |
| gizmo | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Inventor.cs:46 |
| doodad | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Inventor.cs:54 |
| mechanical_experiment | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Inventor.cs:62 |
| alchemical_experiment | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Inventor.cs:70 |
| biological_experiment | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Inventor.cs:78 |
| tinkersteel | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:86 |
| witchcloth | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:93 |
| primal_leather | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:100 |
| petrified_wood | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:107 |
| winged_boots | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:114 |
| golem_gauntlets | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:121 |
| mind_goggles | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:128 |
| crit_goggles | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:135 |
| chainsaw | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:142 |
| shield_arm | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:149 |
| triune_shield | Recipe | Root inventor;  | — | — | CostCurrency=GoldIngenuity | — | T10Inventor.cs:156 |
| nightmare_collector | Recipe | Root inventor;  | nightmare_distiller | — | CostTier=12; CostCurrency=GoldIngenuity | — | T10Inventor.cs:163 |
| currency_exchange | Utility | ; Previous inventor | — | — | Inherited/default | — | T10Inventor.cs:172 |
| currency_exchange_tax | Utility | ; Previous currency_exchange | — | — | CostMultiplier=8.0 | — | T10Inventor.cs:179 |

```csharp
25: TechNodeHelper.AddDefaultUpgrades("Inventor");
26: TechNode.Get("inventor_productivity").CostCurrency = CurrencyCollection.GoldIngenuity;
27: TechNode.Get("inventor_automation_2").CostCurrency = CurrencyCollection.GoldIngenuity;
28: TechNode.Get("inventor_quality").CostCurrency = CurrencyCollection.GoldIngenuity;
29: TechNode.Get("inventor_automation_3").CostCurrency = CurrencyCollection.GoldIngenuity;
```

## Scribe branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| scribe | FlowElement | ; Previous inventor | — | — | Inherited/default | blank_vellum, blank_tome | T10Scribe.cs:10 |
| blank_vellum | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Scribe.cs:24 |
| blank_tome | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity; CostMultiplier=0.5 | — | T10Scribe.cs:32 |
| mad_scribblings | Recipe | Root scribe;  | — | — | CostCurrency=GoldMana; CostMultiplier=0.5 | — | T10Scribe.cs:40 |
| scroll_of_healing | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:48 |
| scroll_of_aoe_healing | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:55 |
| scroll_of_damage | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:62 |
| scroll_of_energy | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:69 |
| tome_of_health | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:76 |
| tome_of_stats | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:83 |
| tome_of_energy | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:90 |
| cr_survivalist | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:97 |
| cr_pyromancer | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:104 |
| cr_lithomancer | Recipe | Root scribe;  | — | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:111 |
| decoded_writings | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:118 |
| demonsteel_helm | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:126 |
| demonsteel_armor | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:134 |
| infected_shield | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:142 |
| hellish_mask | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:150 |
| hellish_cover | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:158 |
| archmage_hat | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:166 |
| archmage_robe | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:174 |
| prophet_hood | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:182 |
| prophet_robe | Recipe | Root scribe;  | dungeon_catacombs | — | CostCurrency=GoldIngenuity | — | T10Scribe.cs:190 |
| library | FlowElement | ; Previous scribe | — | — | Inherited/default | — | T10Scribe.cs:198 |

```csharp
23: TechNodeHelper.AddDefaultUpgrades("Scribe");
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T10Inventor.cs:10`
- `Assets.Source.Player.Tech/T10Inventor.cs:30`
- `Assets.Source.Player.Tech/T10Inventor.cs:38`
- `Assets.Source.Player.Tech/T10Inventor.cs:46`
- `Assets.Source.Player.Tech/T10Inventor.cs:54`
- `Assets.Source.Player.Tech/T10Inventor.cs:62`
- `Assets.Source.Player.Tech/T10Inventor.cs:70`
- `Assets.Source.Player.Tech/T10Inventor.cs:78`
- `Assets.Source.Player.Tech/T10Inventor.cs:86`
- `Assets.Source.Player.Tech/T10Inventor.cs:93`
- `Assets.Source.Player.Tech/T10Inventor.cs:100`
- `Assets.Source.Player.Tech/T10Inventor.cs:107`
- `Assets.Source.Player.Tech/T10Inventor.cs:114`
- `Assets.Source.Player.Tech/T10Inventor.cs:121`
- `Assets.Source.Player.Tech/T10Inventor.cs:128`
- `Assets.Source.Player.Tech/T10Inventor.cs:135`
- `Assets.Source.Player.Tech/T10Inventor.cs:142`
- `Assets.Source.Player.Tech/T10Inventor.cs:149`
- `Assets.Source.Player.Tech/T10Inventor.cs:156`
- `Assets.Source.Player.Tech/T10Inventor.cs:163`
- `Assets.Source.Player.Tech/T10Inventor.cs:172`
- `Assets.Source.Player.Tech/T10Inventor.cs:179`
- `Assets.Source.Player.Tech/T10Scribe.cs:10`
- `Assets.Source.Player.Tech/T10Scribe.cs:24`
- `Assets.Source.Player.Tech/T10Scribe.cs:32`
- `Assets.Source.Player.Tech/T10Scribe.cs:40`
- `Assets.Source.Player.Tech/T10Scribe.cs:48`
- `Assets.Source.Player.Tech/T10Scribe.cs:55`
- `Assets.Source.Player.Tech/T10Scribe.cs:62`
- `Assets.Source.Player.Tech/T10Scribe.cs:69`
- `Assets.Source.Player.Tech/T10Scribe.cs:76`
- `Assets.Source.Player.Tech/T10Scribe.cs:83`
- `Assets.Source.Player.Tech/T10Scribe.cs:90`
- `Assets.Source.Player.Tech/T10Scribe.cs:97`
- `Assets.Source.Player.Tech/T10Scribe.cs:104`
- `Assets.Source.Player.Tech/T10Scribe.cs:111`
- `Assets.Source.Player.Tech/T10Scribe.cs:118`
- `Assets.Source.Player.Tech/T10Scribe.cs:126`
- `Assets.Source.Player.Tech/T10Scribe.cs:134`
- `Assets.Source.Player.Tech/T10Scribe.cs:142`
- `Assets.Source.Player.Tech/T10Scribe.cs:150`
- `Assets.Source.Player.Tech/T10Scribe.cs:158`
- `Assets.Source.Player.Tech/T10Scribe.cs:166`
- `Assets.Source.Player.Tech/T10Scribe.cs:174`
- `Assets.Source.Player.Tech/T10Scribe.cs:182`
- `Assets.Source.Player.Tech/T10Scribe.cs:190`
- `Assets.Source.Player.Tech/T10Scribe.cs:198`
