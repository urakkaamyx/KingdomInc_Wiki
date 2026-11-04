# Technology tier 9: Alchemy and arena

Alchemist follows Jeweler and grants healing_potion. Feral Den research follows it. Arena requires Eastern war stage 4; its branch opens Yensburg war, Temple research, and associated support.

## Branch overview

Alchemist follows Jeweler and grants healing_potion. Feral Den research follows it. Arena requires Eastern war stage 4; its branch opens Yensburg war, Temple research, and associated support.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Alchemist branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alchemist | FlowElement | ; Previous jeweler | — | — | CostTier=9 | healing_potion | T9Alchemist.cs:10 |
| dungeon_feral_den | Dungeon | ; Previous alchemist | — | — | Inherited/default | — | T9Alchemist.cs:24 |
| attuned_catalyst | Recipe | Root alchemist;  | — | — | Inherited/default | — | T9Alchemist.cs:35 |
| transmute_metals | Recipe | Root alchemist;  | — | — | Inherited/default | — | T9Alchemist.cs:41 |
| healing_potion | Recipe | Root alchemist;  | — | — | Inherited/default | — | T9Alchemist.cs:47 |
| energy_potion | Recipe | Root alchemist;  | — | — | Inherited/default | — | T9Alchemist.cs:53 |
| identify_plants | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:59 |
| fire_resist_potion | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:66 |
| shadow_resist_potion | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:73 |
| poison_resist_potion | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:80 |
| armor_potion | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:87 |
| greater_healing_potion | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:94 |
| stats_potion | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:101 |
| swiftness_potion | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:108 |
| regen_potion | Recipe | Root alchemist;  | dungeon_feral_den | — | Inherited/default | — | T9Alchemist.cs:115 |

```csharp
23: TechNodeHelper.AddDefaultUpgrades("Alchemist");
```

## Arena branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| arena | FlowElement | ; Previous alchemist | — | eastern war stage 4 | CostTier=9; CostCurrency=GoldDucat | — | T9Arena.cs:11 |
| arena_cashier | UpgradeSlot | ; Previous arena_automation | — | — | Inherited/default | — | T9Arena.cs:26 |
| arena_blood_sport | UpgradeSlot | ; Previous arena_automation_2 | — | — | Inherited/default | — | T9Arena.cs:38 |
| war_effort_yensburg | War | ; Previous arena | — | — | CostTier=10; CostCurrency=GoldDucat; CostMultiplier=2.0 | — | T9Arena.cs:50 |
| dungeon_temple | Dungeon | ; Previous arena | — | — | Inherited/default | — | T9Arena.cs:65 |
| hoard | FlowElement | ; Previous dungeon_temple | — | — | Inherited/default | — | T9Arena.cs:76 |

```csharp
23: TechNode.Add(TechNodeHelper.UpgradeWorker("Arena"));
24: TechNode.Add(TechNodeHelper.UpgradeSlot2("Arena", allowMultiWorkers: false));
25: TechNode.Add(TechNodeHelper.UpgradeSlot3("Arena"));
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T9Alchemist.cs:10`
- `Assets.Source.Player.Tech/T9Alchemist.cs:24`
- `Assets.Source.Player.Tech/T9Alchemist.cs:35`
- `Assets.Source.Player.Tech/T9Alchemist.cs:41`
- `Assets.Source.Player.Tech/T9Alchemist.cs:47`
- `Assets.Source.Player.Tech/T9Alchemist.cs:53`
- `Assets.Source.Player.Tech/T9Alchemist.cs:59`
- `Assets.Source.Player.Tech/T9Alchemist.cs:66`
- `Assets.Source.Player.Tech/T9Alchemist.cs:73`
- `Assets.Source.Player.Tech/T9Alchemist.cs:80`
- `Assets.Source.Player.Tech/T9Alchemist.cs:87`
- `Assets.Source.Player.Tech/T9Alchemist.cs:94`
- `Assets.Source.Player.Tech/T9Alchemist.cs:101`
- `Assets.Source.Player.Tech/T9Alchemist.cs:108`
- `Assets.Source.Player.Tech/T9Alchemist.cs:115`
- `Assets.Source.Player.Tech/T9Arena.cs:11`
- `Assets.Source.Player.Tech/T9Arena.cs:26`
- `Assets.Source.Player.Tech/T9Arena.cs:38`
- `Assets.Source.Player.Tech/T9Arena.cs:50`
- `Assets.Source.Player.Tech/T9Arena.cs:65`
- `Assets.Source.Player.Tech/T9Arena.cs:76`
