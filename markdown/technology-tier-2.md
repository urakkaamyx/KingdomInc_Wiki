# Technology tier 2: Requisitions and crafts

Requisition Office starts the second currency economy and uses Gold-only research despite cost tier 2. Tailor follows it, then Carpenter and Leatherworker branch into shields, bows, staffs, robes, cloth armor, and strings.

## Branch overview

Requisition Office starts the second currency economy and uses Gold-only research despite cost tier 2. Tailor follows it, then Carpenter and Leatherworker branch into shields, bows, staffs, robes, cloth armor, and strings.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Carpenter branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| carpenter | FlowElement | ; Previous tailor | — | — | Inherited/default | simple_wooden_shield | T2Carpenter.cs:10 |
| softwood_bow | Recipe | Root carpenter;  | rough_string | — | Inherited/default | — | T2Carpenter.cs:21 |
| initiate_staff | Recipe | Root carpenter;  | mine_sapphire | — | Inherited/default | — | T2Carpenter.cs:28 |
| softwood_warstaff | Recipe | Root carpenter;  | — | — | Inherited/default | — | T2Carpenter.cs:35 |
| simple_wooden_shield | Recipe | Root carpenter;  | — | — | Inherited/default | — | T2Carpenter.cs:41 |
| reinforced_wooden_shield | Recipe | Root carpenter;  | — | — | Inherited/default | — | T2Carpenter.cs:47 |
| wood_plank | Recipe | Root carpenter;  | forest | — | CostTier=4 | — | T2Carpenter.cs:53 |
| wild_staff | Recipe | Root carpenter;  | forest_bone | — | CostTier=4 | — | T2Carpenter.cs:61 |
| ancient_wood_plank | Recipe | Root carpenter;  | forest_ancient_wood | — | CostTier=6 | — | T2Carpenter.cs:69 |
| ancient_wood_staff | Recipe | Root carpenter;  | ancient_wood_plank | — | CostTier=6 | — | T2Carpenter.cs:77 |
| ancient_wood_bow | Recipe | Root carpenter;  | ancient_wood_plank | — | CostTier=6 | — | T2Carpenter.cs:85 |
| ancient_shield | Recipe | Root carpenter;  | ancient_wood_plank | — | CostTier=6 | — | T2Carpenter.cs:93 |
| ancient_int_staff | Recipe | Root carpenter;  | dungeon | — | CostTier=8 | — | T2Carpenter.cs:101 |
| ancient_wis_staff | Recipe | Root carpenter;  | dungeon | — | CostTier=8 | — | T2Carpenter.cs:109 |
| trueshot_bow | Recipe | Root carpenter;  | inventor | — | CostTier=10 | — | T2Carpenter.cs:117 |
| petrified_shield | Recipe | Root carpenter;  | inventor | — | CostTier=10 | — | T2Carpenter.cs:125 |
| archmage_staff | Recipe | Root carpenter;  | inventor | — | CostTier=10 | — | T2Carpenter.cs:133 |
| archbishop_staff | Recipe | Root carpenter;  | inventor | — | CostTier=10 | — | T2Carpenter.cs:141 |
| coffin | Recipe | Root carpenter;  | graveyard | — | CostTier=11 | — | T2Carpenter.cs:149 |

```csharp
157: TechNodeHelper.AddDefaultUpgrades("Carpenter");
```

## Leatherworker branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| leatherworker | FlowElement | ; Previous tailor | — | — | Inherited/default | rough_string | T2Leatherworker.cs:10 |
| rough_string | Recipe | Root leatherworker;  | — | — | Inherited/default | — | T2Leatherworker.cs:21 |
| rough_vest | Recipe | Root leatherworker;  | — | — | Inherited/default | — | T2Leatherworker.cs:27 |
| rough_leather_hat | Recipe | Root leatherworker;  | — | — | Inherited/default | — | T2Leatherworker.cs:33 |
| rough_leather | Recipe | Root leatherworker;  | forest | — | Inherited/default | — | T2Leatherworker.cs:39 |
| supple_string | Recipe | Root leatherworker;  | enchanter | — | CostTier=6 | — | T2Leatherworker.cs:46 |
| embossed_vest | Recipe | Root leatherworker;  | embossed_leather | — | CostTier=7 | — | T2Leatherworker.cs:54 |
| embossed_hat | Recipe | Root leatherworker;  | embossed_leather | — | CostTier=7 | — | T2Leatherworker.cs:62 |
| primal_string | Recipe | Root leatherworker;  | inventor | — | CostTier=10 | — | T2Leatherworker.cs:70 |
| primal_cover | Recipe | Root leatherworker;  | inventor | — | CostTier=10 | — | T2Leatherworker.cs:78 |
| primal_mask | Recipe | Root leatherworker;  | inventor | — | CostTier=10 | — | T2Leatherworker.cs:86 |

```csharp
94: TechNodeHelper.AddDefaultUpgrades("Leatherworker");
```

## RequisitionOffice branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| requisition_office | FlowElement | ; Previous supply_depot | — | — | CostTier=2; CostCurrency=Gold; CostMultiplier=3.0 | — | T2RequisitionOffice.cs:13 |
| requisition_office_cashier | UpgradeSlot | ; Previous requisition_office_automation | — | — | Inherited/default | — | T2RequisitionOffice.cs:28 |
| requisition_office_passive | UpgradeSlot | ; Previous requisition_office_automation_2 | war_effort | — | Inherited/default | — | T2RequisitionOffice.cs:42 |
| requisition_office_reroll | Utility | Root requisition_office;  | — | — | Inherited/default | — | T2RequisitionOffice.cs:54 |
| requisition_office_contract | Utility | ; Previous requisition_office_reroll | — | — | Inherited/default | — | T2RequisitionOffice.cs:61 |
| requisition_office_contract_2 | Utility | ; Previous requisition_office_contract | war_effort | — | CostTier=4 | — | T2RequisitionOffice.cs:72 |
| requisition_office_contract_3 | Utility | ; Previous requisition_office_contract | adventurers_guild | — | CostTier=5 | — | T2RequisitionOffice.cs:85 |
| requisition_office_contract_4 | Utility | ; Previous requisition_office_contract_2 | enchanter | — | CostTier=6; CostCurrency=GoldMana | — | T2RequisitionOffice.cs:98 |
| inspector | FlowElement | ; Previous requisition_office | — | — | Inherited/default | — | T2RequisitionOffice.cs:112 |
| incinerator | FlowElement | ; Previous requisition_office | — | — | Inherited/default | — | T2RequisitionOffice.cs:119 |
| easy_node_upgrade | Utility | ; Previous requisition_office | — | — | Inherited/default | — | T2RequisitionOffice.cs:126 |
| item_list | Utility | ; Previous requisition_office | — | — | CostMultiplier=3.0 | — | T2RequisitionOffice.cs:133 |

```csharp
27: TechNode.Add(TechNodeHelper.UpgradeWorker("RequisitionOffice")).CostMultiplier = 3.0;
40: TechNode.Add(TechNodeHelper.UpgradeSlot2("RequisitionOffice", allowMultiWorkers: false));
41: TechNode.Add(TechNodeHelper.UpgradeSlot3("RequisitionOffice"));
```

## Tailor branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tailor | FlowElement | ; Previous requisition_office | — | — | Inherited/default | linen_padding | T2Tailor.cs:10 |
| linen_padding | Recipe | Root tailor;  | — | — | Inherited/default | — | T2Tailor.cs:21 |
| simple_robe | Recipe | Root tailor;  | — | — | Inherited/default | — | T2Tailor.cs:27 |
| initiate_hat | Recipe | Root tailor;  | — | — | Inherited/default | — | T2Tailor.cs:33 |
| linen_cloth | Recipe | Root tailor;  | farm_flax | — | Inherited/default | — | T2Tailor.cs:39 |
| cotton_cloth | Recipe | Root tailor;  | farm_cotton | — | Inherited/default | — | T2Tailor.cs:46 |
| cotton_robe | Recipe | Root tailor;  | embroidered_cotton | — | CostTier=7 | — | T2Tailor.cs:53 |
| cotton_hat | Recipe | Root tailor;  | embroidered_cotton | — | CostTier=7 | — | T2Tailor.cs:61 |
| witch_robe | Recipe | Root tailor;  | inventor | — | CostTier=10 | — | T2Tailor.cs:69 |
| witch_hood | Recipe | Root tailor;  | inventor | — | CostTier=10 | — | T2Tailor.cs:77 |

```csharp
85: TechNodeHelper.AddDefaultUpgrades("Tailor");
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T2Carpenter.cs:10`
- `Assets.Source.Player.Tech/T2Carpenter.cs:21`
- `Assets.Source.Player.Tech/T2Carpenter.cs:28`
- `Assets.Source.Player.Tech/T2Carpenter.cs:35`
- `Assets.Source.Player.Tech/T2Carpenter.cs:41`
- `Assets.Source.Player.Tech/T2Carpenter.cs:47`
- `Assets.Source.Player.Tech/T2Carpenter.cs:53`
- `Assets.Source.Player.Tech/T2Carpenter.cs:61`
- `Assets.Source.Player.Tech/T2Carpenter.cs:69`
- `Assets.Source.Player.Tech/T2Carpenter.cs:77`
- `Assets.Source.Player.Tech/T2Carpenter.cs:85`
- `Assets.Source.Player.Tech/T2Carpenter.cs:93`
- `Assets.Source.Player.Tech/T2Carpenter.cs:101`
- `Assets.Source.Player.Tech/T2Carpenter.cs:109`
- `Assets.Source.Player.Tech/T2Carpenter.cs:117`
- `Assets.Source.Player.Tech/T2Carpenter.cs:125`
- `Assets.Source.Player.Tech/T2Carpenter.cs:133`
- `Assets.Source.Player.Tech/T2Carpenter.cs:141`
- `Assets.Source.Player.Tech/T2Carpenter.cs:149`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:10`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:21`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:27`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:33`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:39`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:46`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:54`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:62`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:70`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:78`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:86`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:13`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:28`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:42`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:54`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:61`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:72`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:85`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:98`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:112`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:119`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:126`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:133`
- `Assets.Source.Player.Tech/T2Tailor.cs:10`
- `Assets.Source.Player.Tech/T2Tailor.cs:21`
- `Assets.Source.Player.Tech/T2Tailor.cs:27`
- `Assets.Source.Player.Tech/T2Tailor.cs:33`
- `Assets.Source.Player.Tech/T2Tailor.cs:39`
- `Assets.Source.Player.Tech/T2Tailor.cs:46`
- `Assets.Source.Player.Tech/T2Tailor.cs:53`
- `Assets.Source.Player.Tech/T2Tailor.cs:61`
- `Assets.Source.Player.Tech/T2Tailor.cs:69`
- `Assets.Source.Player.Tech/T2Tailor.cs:77`
