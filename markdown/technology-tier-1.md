# Technology tier 1: Foundations

Mine, Forge, Shop, Blacksmith, and Supply Depot establish resources, smelting, sales, equipment, and purchased supplies. Mine and Forge are starting grants. Shop is free but follows Forge. Supply Depot requires both Blacksmith and Mine automation.

## Branch overview

Mine, Forge, Shop, Blacksmith, and Supply Depot establish resources, smelting, sales, equipment, and purchased supplies. Mine and Forge are starting grants. Shop is free but follows Forge. Supply Depot requires both Blacksmith and Mine automation.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Blacksmith branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| blacksmith | FlowElement | ; Previous forge | — | — | CostMultiplier=0.5 | iron_armor | T1Blacksmith.cs:11 |
| iron_armor | Recipe | Root blacksmith;  | — | — | Inherited/default | — | T1Blacksmith.cs:24 |
| iron_helm | Recipe | Root blacksmith;  | — | — | Inherited/default | — | T1Blacksmith.cs:30 |
| iron_sword | Recipe | Root blacksmith;  | supply_depot | — | Inherited/default | — | T1Blacksmith.cs:36 |
| iron_dagger | Recipe | Root blacksmith;  | supply_depot | — | Inherited/default | — | T1Blacksmith.cs:43 |
| iron_greatsword | Recipe | Root blacksmith;  | rough_string | — | CostTier=2 | — | T1Blacksmith.cs:50 |
| iron_battleaxe | Recipe | Root blacksmith;  | rough_string | — | CostTier=2 | — | T1Blacksmith.cs:58 |
| gold_sword | Recipe | Root blacksmith;  | gold_ingot | — | CostTier=3 | — | T1Blacksmith.cs:66 |
| gold_armor | Recipe | Root blacksmith;  | gold_ingot, silver_ingot | — | CostTier=3 | — | T1Blacksmith.cs:74 |
| gold_crown | Recipe | Root blacksmith;  | gold_ingot, mine_sapphire | — | CostTier=3 | — | T1Blacksmith.cs:82 |
| iron_rapier | Recipe | Root blacksmith;  | forest_bone, forest_resin | — | CostTier=4 | — | T1Blacksmith.cs:90 |
| ancient_woodcutter | Recipe | Root blacksmith;  | enchanter | — | CostTier=6 | — | T1Blacksmith.cs:98 |
| arcanium_armor | Recipe | Root blacksmith;  | arcanium_ingot | — | CostTier=6 | — | T1Blacksmith.cs:106 |
| arcanium_helm | Recipe | Root blacksmith;  | arcanium_ingot | — | CostTier=6 | — | T1Blacksmith.cs:114 |
| arcanium_sword | Recipe | Root blacksmith;  | arcanium_ingot | — | CostTier=6 | — | T1Blacksmith.cs:122 |
| arcanium_dagger | Recipe | Root blacksmith;  | arcanium_ingot | — | CostTier=6 | — | T1Blacksmith.cs:130 |
| arcanium_greatsword | Recipe | Root blacksmith;  | arcanium_ingot | — | CostTier=6 | — | T1Blacksmith.cs:138 |
| arcanium_battleaxe | Recipe | Root blacksmith;  | arcanium_ingot | — | CostTier=6 | — | T1Blacksmith.cs:146 |
| tinkersteel_armor | Recipe | Root blacksmith;  | inventor | — | CostTier=10 | — | T1Blacksmith.cs:154 |
| tinkersteel_helm | Recipe | Root blacksmith;  | inventor | — | CostTier=10 | — | T1Blacksmith.cs:162 |
| tinkersteel_sword | Recipe | Root blacksmith;  | inventor | — | CostTier=10 | — | T1Blacksmith.cs:170 |
| tinkersteel_dagger | Recipe | Root blacksmith;  | inventor | — | CostTier=10 | — | T1Blacksmith.cs:178 |
| tinkersteel_rapier | Recipe | Root blacksmith;  | inventor | — | CostTier=10 | — | T1Blacksmith.cs:186 |
| tinkersteel_greatsword | Recipe | Root blacksmith;  | inventor | — | CostTier=10 | — | T1Blacksmith.cs:194 |
| tinkersteel_axe | Recipe | Root blacksmith;  | inventor | — | CostTier=10 | — | T1Blacksmith.cs:202 |
| nightmare_casing | Recipe | Root blacksmith;  | nightmare_distiller | — | CostTier=12 | — | T1Blacksmith.cs:210 |
| unlock_picker | Utility | ; Previous blacksmith | — | — | CostMultiplier=2.0 | — | T1Blacksmith.cs:218 |
| clone_tool | Utility | ; Previous unlock_picker | requisition_office | — | CostTier=2; CostMultiplier=2.0 | — | T1Blacksmith.cs:226 |
| unlock_area_move | Utility | ; Previous unlock_picker | — | — | CostMultiplier=2.0 | — | T1Blacksmith.cs:240 |
| container_clone | Utility | ; Previous clone_tool | tech_deco | — | Inherited/default | — | T1Blacksmith.cs:252 |

```csharp
23: TechNodeHelper.AddDefaultUpgrades("Blacksmith");
```

## Forge branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| forge | FlowElement | ; Previous mine | — | — | CostMultiplier=0.0 | — | T1Forge.cs:10 |
| iron_ingot | Recipe | Root forge;  | — | — | CostMultiplier=0.0 | — | T1Forge.cs:18 |
| gold_ingot | Recipe | Root forge;  | mine_gold_ore | — | CostTier=3 | — | T1Forge.cs:25 |
| silver_ingot | Recipe | Root forge;  | mine_silver_ore | — | CostTier=3 | — | T1Forge.cs:33 |

```csharp
41: TechNodeHelper.AddDefaultUpgrades("Forge", hasEquipment: false);
```

## Mine branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mine | FlowElement | ;  | — | — | CostTier=1; CostMultiplier=0.0 | mine_iron_ore | T1Mine.cs:11 |
| dev_item_spawner | FlowElement | ;  | — | Developer-only | CostTier=1; CostMultiplier=0.0 | — | T1Mine.cs:23 |
| mine_iron_ore | Resource | Root mine;  | — | — | Inherited/default | — | T1Mine.cs:31 |
| mine_sapphire | Resource | Root mine;  | requisition_office | — | CostTier=2 | — | T1Mine.cs:37 |
| mine_gold_ore | Resource | Root mine;  | engraver | — | CostTier=3 | — | T1Mine.cs:49 |
| mine_silver_ore | Resource | Root mine;  | engraver | — | CostTier=3 | — | T1Mine.cs:61 |
| tech_deco | Decoration | ; Previous mine | — | — | Inherited/default | — | T1Mine.cs:81 |
| deco_label | Decoration | ; Previous tech_deco | — | — | Inherited/default | — | T1Mine.cs:96 |
| deco_sticker | Decoration | ; Previous deco_label | — | — | Inherited/default | — | T1Mine.cs:103 |

```csharp
73: TechNodeHelper.AddDefaultUpgrades("Mine", hasEquipment: false, hasEnhancements: false, multiWorkerAllowed: true, "MineArtisan");
74: TechNode techNode = TechNode.Get("mine_automation");
75: TechNode.OnTechNodeUnlock onUnlock = techNode.OnUnlock;
76: techNode.OnUnlock = (GamePlayer ply) =>
79: onUnlock(ply);
```

## Shop branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| shop | FlowElement | ; Previous forge | — | — | CostMultiplier=0.0 | — | T1Shop.cs:12 |
| shop_expansion | Utility | Root shop;  | enchanter | — | CostTier=7 | — | T1Shop.cs:20 |
| shop_cashier | UpgradeSlot | ; Previous shop_automation | — | — | Inherited/default | — | T1Shop.cs:37 |

```csharp
36: TechNode.Add(TechNodeHelper.UpgradeWorker("Shop")).CostMultiplier = 3.0;
49: TechNode.Add(TechNodeHelper.UpgradeSlot2("Shop"));
50: TechNode.Add(TechNodeHelper.UpgradeCoffers("Shop"));
51: TechNode.Add(TechNodeHelper.UpgradeSlot3("Shop"));
```

## SupplyDepot branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| supply_depot | FlowElement | ; Previous blacksmith | mine_automation | — | Inherited/default | supply_wood_plank | T1SupplyDepot.cs:11 |
| supply_wood_plank | Resource | Root supply_depot;  | — | — | Inherited/default | — | T1SupplyDepot.cs:23 |
| supply_linen_cloth | Resource | Root supply_depot;  | tailor | — | CostTier=2 | — | T1SupplyDepot.cs:33 |
| supply_rough_leather | Resource | Root supply_depot;  | leatherworker | — | CostTier=2 | — | T1SupplyDepot.cs:45 |
| unlock_supply_window | Utility | ; Previous supply_depot | — | — | Inherited/default | — | T1SupplyDepot.cs:58 |
| distributor | FlowElement | ; Previous supply_depot | — | — | Inherited/default | — | T1SupplyDepot.cs:70 |
| collector | FlowElement | ; Previous distributor | — | — | Inherited/default | — | T1SupplyDepot.cs:77 |

```csharp
57: TechNodeHelper.AddDefaultUpgrades("SupplyDepot", hasEquipment: false, hasEnhancements: false, multiWorkerAllowed: true, "ResArtisan");
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:11`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:24`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:30`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:36`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:43`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:50`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:58`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:66`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:74`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:82`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:90`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:98`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:106`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:114`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:122`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:130`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:138`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:146`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:154`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:162`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:170`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:178`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:186`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:194`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:202`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:210`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:218`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:226`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:240`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:252`
- `Assets.Source.Player.Tech/T1Forge.cs:10`
- `Assets.Source.Player.Tech/T1Forge.cs:18`
- `Assets.Source.Player.Tech/T1Forge.cs:25`
- `Assets.Source.Player.Tech/T1Forge.cs:33`
- `Assets.Source.Player.Tech/T1Mine.cs:11`
- `Assets.Source.Player.Tech/T1Mine.cs:23`
- `Assets.Source.Player.Tech/T1Mine.cs:31`
- `Assets.Source.Player.Tech/T1Mine.cs:37`
- `Assets.Source.Player.Tech/T1Mine.cs:49`
- `Assets.Source.Player.Tech/T1Mine.cs:61`
- `Assets.Source.Player.Tech/T1Mine.cs:81`
- `Assets.Source.Player.Tech/T1Mine.cs:96`
- `Assets.Source.Player.Tech/T1Mine.cs:103`
- `Assets.Source.Player.Tech/T1Shop.cs:12`
- `Assets.Source.Player.Tech/T1Shop.cs:20`
- `Assets.Source.Player.Tech/T1Shop.cs:37`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:11`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:23`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:33`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:45`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:58`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:70`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:77`
