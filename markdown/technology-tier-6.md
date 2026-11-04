# Technology tier 6: Recovery and magic

Inn follows Quest Board, Enchanter follows Inn, and Disenchanter follows Enchanter. This branch adds recovery, Mana, enchanting, disenchanting, enhanced materials, and Eastern war research. Individual upgrades can use Gold plus Mana instead of normal tier currency.

## Branch overview

Inn follows Quest Board, Enchanter follows Inn, and Disenchanter follows Enchanter. This branch adds recovery, Mana, enchanting, disenchanting, enhanced materials, and Eastern war research. Individual upgrades can use Gold plus Mana instead of normal tier currency.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Disenchanter branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| disenchanter | FlowElement | ; Previous enchanter | — | — | CostMultiplier=1.0 | — | T6Disenchanter.cs:10 |
| disenchanter_mana | UpgradeSlot | ; Previous disenchanter_automation | — | — | CostCurrency=GoldMana | — | T6Disenchanter.cs:19 |
| disenchanter_passive | UpgradeSlot | ; Previous disenchanter_automation_2 | — | — | CostCurrency=GoldMana | — | T6Disenchanter.cs:33 |

```csharp
18: TechNode.Add(TechNodeHelper.UpgradeWorker("Disenchanter")).CostCurrency = CurrencyCollection.GoldMana;
32: TechNode.Add(TechNodeHelper.UpgradeSlot2("Disenchanter")).CostCurrency = CurrencyCollection.GoldMana;
45: TechNode.Add(TechNodeHelper.UpgradeSlot3("Disenchanter")).CostCurrency = CurrencyCollection.GoldMana;
```

## Enchanter branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| enchanter | FlowElement | ; Previous inn | — | — | CostMultiplier=6.0 | — | T6Enchanter.cs:11 |
| enhance_multiple | Utility | Root enchanter;  | — | — | CostCurrency=GoldMana; CostMultiplier=6.0 | — | T6Enchanter.cs:20 |
| arcanium_ingot | Recipe | Root enchanter;  | — | — | Inherited/default | — | T6Enchanter.cs:30 |
| crystal_mana | Recipe | Root enchanter;  | — | — | Inherited/default | — | T6Enchanter.cs:36 |
| enchanted_cotton_thread | Recipe | Root enchanter;  | cotton_cloth | — | Inherited/default | — | T6Enchanter.cs:42 |
| enchant_food_quality | Recipe | Root enchanter;  | — | — | Inherited/default | — | T6Enchanter.cs:49 |
| enchant_weapon_power | Recipe | Root enchanter;  | — | — | Inherited/default | — | T6Enchanter.cs:55 |
| enchant_armor_energy | Recipe | Root enchanter;  | — | — | Inherited/default | — | T6Enchanter.cs:61 |
| enchant_armor_armor | Recipe | Root enchanter;  | — | — | Inherited/default | — | T6Enchanter.cs:67 |
| enchant_armor_stats | Recipe | Root enchanter;  | — | — | Inherited/default | — | T6Enchanter.cs:73 |
| enchant_shield_armor | Recipe | Root enchanter;  | — | — | Inherited/default | — | T6Enchanter.cs:79 |
| enchant_armor_shadow_resist | Recipe | Root enchanter;  | butcher_stalker | — | Inherited/default | — | T6Enchanter.cs:85 |
| enchant_weapon_crit | Recipe | Root enchanter;  | butcher_stalker | — | Inherited/default | — | T6Enchanter.cs:92 |
| enchant_armor_strength_skill_crit | Recipe | Root enchanter;  | hamburger | — | Inherited/default | — | T6Enchanter.cs:99 |
| annihilate_gemstone | Recipe | Root enchanter;  | dungeon | — | CostTier=8 | — | T6Enchanter.cs:106 |
| enchant_item_quality | Recipe | Root enchanter;  | dungeon_temple | — | CostTier=9; CostCurrency=GoldMana | — | T6Enchanter.cs:114 |
| symbiote_breeding | Recipe | Root enchanter;  | dungeon_temple | — | CostTier=9; CostCurrency=GoldMana | — | T6Enchanter.cs:123 |
| enchanted_ink | Recipe | Root enchanter;  | scribe | — | CostTier=10; CostCurrency=GoldMana; CostMultiplier=0.5 | — | T6Enchanter.cs:132 |
| reconstructed_nightmare | Recipe | Root enchanter;  | nightmare_distiller | — | CostTier=12; CostCurrency=GoldMana | — | T6Enchanter.cs:142 |
| refiner | FlowElement | ; Previous enchanter | — | — | CostCurrency=GoldMana; CostMultiplier=2.0 | — | T6Enchanter.cs:151 |
| critical_craft | Utility | ; Previous refiner | — | — | CostCurrency=GoldMana; CostMultiplier=6.0 | — | T6Enchanter.cs:160 |
| refiner_mana | Utility | ; Previous refiner | — | — | CostCurrency=GoldMana; CostMultiplier=6.0 | — | T6Enchanter.cs:169 |
| refiner_demon | Utility | ; Previous refiner_mana | summoning_circle | — | CostTier=8; CostMultiplier=3.0 | — | T6Enchanter.cs:185 |
| refiner_human | Utility | ; Previous refiner_demon | necromancer | — | CostTier=11; CostMultiplier=3.0 | — | T6Enchanter.cs:195 |
| war_effort_east | War | ; Previous enchanter | — | — | CostCurrency=GoldRing; CostMultiplier=8.0 | — | T6Enchanter.cs:205 |
| adv_to_war | Utility | ; Previous war_effort_east | — | — | CostMultiplier=3.0 | — | T6Enchanter.cs:219 |

```csharp
29: TechNodeHelper.AddDefaultUpgrades("Enchanter", hasEquipment: true, hasEnhancements: true);
```

## Inn branch

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| inn | FlowElement | ; Previous quest_board | — | — | CostTier=6; CostMultiplier=4.0 | — | T6Inn.cs:10 |
| inn_add_food | Utility | Root inn;  | — | — | Inherited/default | — | T6Inn.cs:20 |

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T6Disenchanter.cs:10`
- `Assets.Source.Player.Tech/T6Disenchanter.cs:19`
- `Assets.Source.Player.Tech/T6Disenchanter.cs:33`
- `Assets.Source.Player.Tech/T6Enchanter.cs:11`
- `Assets.Source.Player.Tech/T6Enchanter.cs:20`
- `Assets.Source.Player.Tech/T6Enchanter.cs:30`
- `Assets.Source.Player.Tech/T6Enchanter.cs:36`
- `Assets.Source.Player.Tech/T6Enchanter.cs:42`
- `Assets.Source.Player.Tech/T6Enchanter.cs:49`
- `Assets.Source.Player.Tech/T6Enchanter.cs:55`
- `Assets.Source.Player.Tech/T6Enchanter.cs:61`
- `Assets.Source.Player.Tech/T6Enchanter.cs:67`
- `Assets.Source.Player.Tech/T6Enchanter.cs:73`
- `Assets.Source.Player.Tech/T6Enchanter.cs:79`
- `Assets.Source.Player.Tech/T6Enchanter.cs:85`
- `Assets.Source.Player.Tech/T6Enchanter.cs:92`
- `Assets.Source.Player.Tech/T6Enchanter.cs:99`
- `Assets.Source.Player.Tech/T6Enchanter.cs:106`
- `Assets.Source.Player.Tech/T6Enchanter.cs:114`
- `Assets.Source.Player.Tech/T6Enchanter.cs:123`
- `Assets.Source.Player.Tech/T6Enchanter.cs:132`
- `Assets.Source.Player.Tech/T6Enchanter.cs:142`
- `Assets.Source.Player.Tech/T6Enchanter.cs:151`
- `Assets.Source.Player.Tech/T6Enchanter.cs:160`
- `Assets.Source.Player.Tech/T6Enchanter.cs:169`
- `Assets.Source.Player.Tech/T6Enchanter.cs:185`
- `Assets.Source.Player.Tech/T6Enchanter.cs:195`
- `Assets.Source.Player.Tech/T6Enchanter.cs:205`
- `Assets.Source.Player.Tech/T6Enchanter.cs:219`
- `Assets.Source.Player.Tech/T6Inn.cs:10`
- `Assets.Source.Player.Tech/T6Inn.cs:20`
