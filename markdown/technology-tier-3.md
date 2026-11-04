# Technology tier 3: Recruiting and war

Barracks follows Carpenter and uses Gold plus Requisition. War Effort unlocks the Forest war and grants its war technology. Engraver follows War Effort and opens engraving plus precious-metal processing.

## Branch overview

Barracks follows Carpenter and uses Gold plus Requisition. War Effort unlocks the Forest war and grants its war technology. Engraver follows War Effort and opens engraving plus precious-metal processing.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Barracks branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| barracks | FlowElement | ; Previous carpenter | — | — | CostTier=3; CostCurrency=GoldRequisition; CostMultiplier=8.0 | recruit_conscript | T3Barracks.cs:11 |
| recruit_conscript | Resource | Root barracks;  | — | — | Inherited/default | — | T3Barracks.cs:27 |
| outfitter | FlowElement | ; Previous barracks | — | — | CostCurrency=GoldRequisition | — | T3Barracks.cs:33 |
| outfitter_automation | Utility | ; Previous outfitter | — | — | Inherited/default | — | T3Barracks.cs:41 |
| outfitter_skip_replace | Utility | ; Previous outfitter | quest_board | — | CostTier=5; CostCurrency=GoldRing | — | T3Barracks.cs:55 |
| outfitter_timeout | Utility | ; Previous outfitter_automation | — | — | Inherited/default | — | T3Barracks.cs:65 |
| outfitter_2 | Utility | ; Previous outfitter | campfire | Always hidden | Inherited/default | — | T3Barracks.cs:72 |

```csharp
26: TechNodeHelper.AddDefaultUpgrades("Barracks", hasEquipment: false, hasEnhancements: false, multiWorkerAllowed: true, "RecruitArtisan");
```

## Engraver branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| engraver | FlowElement | ; Previous war_effort | — | — | Inherited/default | gold_wire, silver_thread | T3Engraver.cs:10 |
| gold_wire | Recipe | Root engraver;  | — | — | Inherited/default | — | T3Engraver.cs:24 |
| silver_thread | Recipe | Root engraver;  | — | — | Inherited/default | — | T3Engraver.cs:30 |
| engrave_heavy_armor_health | Recipe | Root engraver;  | — | — | Inherited/default | — | T3Engraver.cs:36 |
| engrave_light_armor_health | Recipe | Root engraver;  | — | — | Inherited/default | — | T3Engraver.cs:42 |
| engrave_heavy_armor_armor | Recipe | Root engraver;  | forest_bone | — | Inherited/default | — | T3Engraver.cs:48 |
| engrave_light_armor_armor | Recipe | Root engraver;  | forest_bone | — | Inherited/default | — | T3Engraver.cs:55 |
| engrave_light_armor_dex | Recipe | Root engraver;  | forest_resin | — | Inherited/default | — | T3Engraver.cs:62 |
| engrave_light_armor_mag | Recipe | Root engraver;  | forest_mushroom | — | Inherited/default | — | T3Engraver.cs:69 |
| engrave_light_armor_wis | Recipe | Root engraver;  | forest | — | Inherited/default | — | T3Engraver.cs:76 |
| engrave_weapon_str | Recipe | Root engraver;  | forest_bone | — | Inherited/default | — | T3Engraver.cs:83 |
| engrave_weapon_dex | Recipe | Root engraver;  | forest_resin | — | Inherited/default | — | T3Engraver.cs:90 |
| engrave_weapon_mag | Recipe | Root engraver;  | forest_mushroom | — | Inherited/default | — | T3Engraver.cs:97 |
| engrave_weapon_wis | Recipe | Root engraver;  | forest | — | Inherited/default | — | T3Engraver.cs:104 |
| embroidered_cotton | Recipe | Root engraver;  | enchanted_cotton_thread | — | CostTier=7 | — | T3Engraver.cs:111 |
| embossed_leather | Recipe | Root engraver;  | forest_supple_leather, enchanted_cotton_thread | — | CostTier=7 | — | T3Engraver.cs:119 |
| engrave_jewelry_quality | Recipe | Root engraver;  | jeweler | — | CostTier=8 | — | T3Engraver.cs:127 |
| gilded_coffin | Recipe | Root engraver;  | graveyard | — | CostTier=7 | — | T3Engraver.cs:135 |
| timer_node | FlowElement | ; Previous engraver | — | — | Inherited/default | — | T3Engraver.cs:143 |

```csharp
23: TechNodeHelper.AddDefaultUpgrades("Engraver", hasEquipment: true, hasEnhancements: true);
```

## WarEffort branch

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| war_effort | FlowElement | ; Previous barracks | — | — | CostCurrency=GoldRequisition; CostMultiplier=2.0 | war_effort_forest | T3WarEffort.cs:11 |
| war_effort_forest | War | Root war_effort;  | — | — | Inherited/default | — | T3WarEffort.cs:28 |
| war_effort_passive | Utility | Root war_effort;  | — | — | CostMultiplier=6.0 | — | T3WarEffort.cs:34 |
| single_button | FlowElement | ; Previous war_effort | — | — | CostMultiplier=0.5 | — | T3WarEffort.cs:42 |
| track_switch | FlowElement | ; Previous war_effort | — | — | CostMultiplier=0.5 | — | T3WarEffort.cs:50 |
| track_switch_2 | Utility | ; Previous track_switch | — | — | Inherited/default | — | T3WarEffort.cs:58 |

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T3Barracks.cs:11`
- `Assets.Source.Player.Tech/T3Barracks.cs:27`
- `Assets.Source.Player.Tech/T3Barracks.cs:33`
- `Assets.Source.Player.Tech/T3Barracks.cs:41`
- `Assets.Source.Player.Tech/T3Barracks.cs:55`
- `Assets.Source.Player.Tech/T3Barracks.cs:65`
- `Assets.Source.Player.Tech/T3Barracks.cs:72`
- `Assets.Source.Player.Tech/T3Engraver.cs:10`
- `Assets.Source.Player.Tech/T3Engraver.cs:24`
- `Assets.Source.Player.Tech/T3Engraver.cs:30`
- `Assets.Source.Player.Tech/T3Engraver.cs:36`
- `Assets.Source.Player.Tech/T3Engraver.cs:42`
- `Assets.Source.Player.Tech/T3Engraver.cs:48`
- `Assets.Source.Player.Tech/T3Engraver.cs:55`
- `Assets.Source.Player.Tech/T3Engraver.cs:62`
- `Assets.Source.Player.Tech/T3Engraver.cs:69`
- `Assets.Source.Player.Tech/T3Engraver.cs:76`
- `Assets.Source.Player.Tech/T3Engraver.cs:83`
- `Assets.Source.Player.Tech/T3Engraver.cs:90`
- `Assets.Source.Player.Tech/T3Engraver.cs:97`
- `Assets.Source.Player.Tech/T3Engraver.cs:104`
- `Assets.Source.Player.Tech/T3Engraver.cs:111`
- `Assets.Source.Player.Tech/T3Engraver.cs:119`
- `Assets.Source.Player.Tech/T3Engraver.cs:127`
- `Assets.Source.Player.Tech/T3Engraver.cs:135`
- `Assets.Source.Player.Tech/T3Engraver.cs:143`
- `Assets.Source.Player.Tech/T3WarEffort.cs:11`
- `Assets.Source.Player.Tech/T3WarEffort.cs:28`
- `Assets.Source.Player.Tech/T3WarEffort.cs:34`
- `Assets.Source.Player.Tech/T3WarEffort.cs:42`
- `Assets.Source.Player.Tech/T3WarEffort.cs:50`
- `Assets.Source.Player.Tech/T3WarEffort.cs:58`
