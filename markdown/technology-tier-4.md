# Technology tier 4: Forest production

Forest requires Forest war stage 1. It creates three unassigned workers and one each Hunter, Logger, and Forager, and grants wood-log, wolf-hide, and bird-egg technologies. Campfire opens food preparation. More Forest resources require later Forest war stages.

## Branch overview

Forest requires Forest war stage 1. It creates three unassigned workers and one each Hunter, Logger, and Forager, and grants wood-log, wolf-hide, and bird-egg technologies. Campfire opens food preparation. More Forest resources require later Forest war stages.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Campfire branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| campfire | FlowElement | ; Previous forest | — | — | Inherited/default | cooked_egg | T4Campfire.cs:10 |
| cooked_egg | Recipe | Root campfire;  | — | — | Inherited/default | — | T4Campfire.cs:22 |
| salad | Recipe | Root campfire;  | — | — | Inherited/default | — | T4Campfire.cs:28 |
| boar_steak | Recipe | Root campfire;  | — | — | Inherited/default | — | T4Campfire.cs:34 |
| mushroom_stew | Recipe | Root campfire;  | forest_bone, forest_mushroom | — | Inherited/default | — | T4Campfire.cs:40 |
| cr_beast_master | Recipe | Root campfire;  | scribe | — | CostTier=10; CostCurrency=GoldIngenuity | — | T4Campfire.cs:47 |

```csharp
56: TechNodeHelper.AddDefaultUpgrades("Campfire");
```

## Forest branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| forest | FlowElement | ; Previous war_effort | — | forest war stage 1 | CostTier=4; CostMultiplier=8.0 | forest_wood_log, forest_wolf_hide, forest_bird_egg | T4Forest.cs:14 |
| forest_workforce | Utility | Root forest;  | enchanter | — | CostTier=6; CostCurrency=GoldMana | — | T4Forest.cs:40 |
| forest_wood_log | Resource | Root forest;  | — | — | Inherited/default | — | T4Forest.cs:50 |
| forest_wolf_hide | Resource | Root forest;  | — | — | Inherited/default | — | T4Forest.cs:60 |
| forest_bird_egg | Resource | Root forest;  | — | — | Inherited/default | — | T4Forest.cs:70 |
| forest_lettuce | Resource | Root forest;  | — | — | Inherited/default | — | T4Forest.cs:80 |
| forest_boar_meat | Resource | Root forest;  | — | — | Inherited/default | — | T4Forest.cs:90 |
| forest_resin | Resource | Root forest;  | — | forest war stage 3 | Inherited/default | — | T4Forest.cs:100 |
| forest_bone | Resource | Root forest;  | — | forest war stage 3 | Inherited/default | — | T4Forest.cs:112 |
| forest_mushroom | Resource | Root forest;  | — | forest war stage 3 | Inherited/default | — | T4Forest.cs:124 |
| forest_ancient_wood | Resource | Root forest;  | enchanter | — | CostTier=6 | — | T4Forest.cs:136 |
| forest_supple_leather | Resource | Root forest;  | enchanter | — | CostTier=6 | — | T4Forest.cs:148 |
| forest_wild_onion | Resource | Root forest;  | kitchen | — | CostTier=7 | — | T4Forest.cs:160 |
| manifold | FlowElement | ; Previous forest | — | — | Inherited/default | — | T4Forest.cs:172 |
| buy_menu_search | Utility | ; Previous manifold | — | Always hidden | Inherited/default | — | T4Forest.cs:179 |
| stockpile | FlowElement | ; Previous manifold | — | — | Inherited/default | — | T4Forest.cs:187 |
| stockpile_capacity | Utility | ; Previous stockpile | enchanter | — | CostTier=5; CostCurrency=GoldMana | — | T4Forest.cs:194 |
| stockpile_overflow | Utility | ; Previous stockpile_capacity | — | — | CostCurrency=GoldMana | — | T4Forest.cs:204 |

```csharp
39: TechNodeHelper.AddDefaultUpgrades("Forest", hasEquipment: false, hasEnhancements: false, multiWorkerAllowed: true, "ForestArtisan");
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T4Campfire.cs:10`
- `Assets.Source.Player.Tech/T4Campfire.cs:22`
- `Assets.Source.Player.Tech/T4Campfire.cs:28`
- `Assets.Source.Player.Tech/T4Campfire.cs:34`
- `Assets.Source.Player.Tech/T4Campfire.cs:40`
- `Assets.Source.Player.Tech/T4Campfire.cs:47`
- `Assets.Source.Player.Tech/T4Forest.cs:14`
- `Assets.Source.Player.Tech/T4Forest.cs:40`
- `Assets.Source.Player.Tech/T4Forest.cs:50`
- `Assets.Source.Player.Tech/T4Forest.cs:60`
- `Assets.Source.Player.Tech/T4Forest.cs:70`
- `Assets.Source.Player.Tech/T4Forest.cs:80`
- `Assets.Source.Player.Tech/T4Forest.cs:90`
- `Assets.Source.Player.Tech/T4Forest.cs:100`
- `Assets.Source.Player.Tech/T4Forest.cs:112`
- `Assets.Source.Player.Tech/T4Forest.cs:124`
- `Assets.Source.Player.Tech/T4Forest.cs:136`
- `Assets.Source.Player.Tech/T4Forest.cs:148`
- `Assets.Source.Player.Tech/T4Forest.cs:160`
- `Assets.Source.Player.Tech/T4Forest.cs:172`
- `Assets.Source.Player.Tech/T4Forest.cs:179`
- `Assets.Source.Player.Tech/T4Forest.cs:187`
- `Assets.Source.Player.Tech/T4Forest.cs:194`
- `Assets.Source.Player.Tech/T4Forest.cs:204`
