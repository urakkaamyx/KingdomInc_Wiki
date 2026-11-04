# Technology tier 7: Farming and dining

Farm follows Eastern war research and requires Eastern war stage 1. Kitchen and Butcher produce meals, Restaurant opens Crowns, and several Farm/Kitchen/Butcher upgrades explicitly use Crowns. Portal and luxury-sale support are also declared here.

## Branch overview

Farm follows Eastern war research and requires Eastern war stage 1. Kitchen and Butcher produce meals, Restaurant opens Crowns, and several Farm/Kitchen/Butcher upgrades explicitly use Crowns. Portal and luxury-sale support are also declared here.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Butcher branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| butcher | FlowElement | ; Previous kitchen | — | — | CostMultiplier=3.5 | butcher_cattle | T7Butcher.cs:10 |
| butcher_cattle | Recipe | Root butcher;  | — | — | Inherited/default | — | T7Butcher.cs:28 |
| butcher_salamander | Recipe | Root butcher;  | — | — | Inherited/default | — | T7Butcher.cs:34 |
| butcher_stalker | Recipe | Root butcher;  | — | — | Inherited/default | — | T7Butcher.cs:40 |
| cr_assassin | Recipe | Root butcher;  | scribe | — | CostTier=10; CostCurrency=GoldIngenuity | — | T7Butcher.cs:46 |

```csharp
23: TechNodeHelper.AddDefaultUpgrades("Butcher", hasEquipment: false);
24: TechNode.Get("butcher_automation_2").CostCurrency = CurrencyCollection.GoldCrown;
25: TechNode.Get("butcher_automation_3").CostCurrency = CurrencyCollection.GoldCrown;
26: TechNode.Get("butcher_quality").CostCurrency = CurrencyCollection.GoldCrown;
27: TechNode.Get("butcher_productivity").CostCurrency = CurrencyCollection.GoldCrown;
```

## Farm branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| farm | FlowElement | ; Previous war_effort_east | — | eastern war stage 1 | CostTier=7; CostMultiplier=8.0 | farm_cattle, farm_wheat | T7Farm.cs:15 |
| farm_cattle | Resource | Root farm;  | — | — | Inherited/default | — | T7Farm.cs:40 |
| farm_wheat | Resource | Root farm;  | — | — | Inherited/default | — | T7Farm.cs:50 |
| farm_flax | Resource | Root farm;  | — | — | Inherited/default | — | T7Farm.cs:60 |
| farm_cotton | Resource | Root farm;  | — | — | CostMultiplier=1.5 | — | T7Farm.cs:70 |
| farm_salamander | Resource | Root farm;  | — | — | CostMultiplier=1.5 | — | T7Farm.cs:81 |
| farm_onion | Resource | Root farm;  | — | — | Inherited/default | — | T7Farm.cs:92 |
| farm_stalker | Resource | Root farm;  | — | — | CostMultiplier=1.5 | — | T7Farm.cs:102 |
| farm_soothing_herbs | Resource | Root farm;  | alchemist | — | CostMultiplier=1.5 | — | T7Farm.cs:113 |
| portal | FlowElement | ; Previous farm | — | — | CostCurrency=GoldMana | — | T7Farm.cs:125 |
| portal_cost_reduce | Utility | ; Previous portal | — | — | CostCurrency=GoldMana | — | T7Farm.cs:133 |
| portal_cost_reduce_2 | Utility | ; Previous portal_cost_reduce | inventor | — | CostTier=11; CostCurrency=GoldIngenuity | — | T7Farm.cs:141 |
| portal_unlock_channels | Utility | ; Previous portal | — | — | CostCurrency=GoldMana; CostMultiplier=2.0 | — | T7Farm.cs:151 |
| portal_overflow | Utility | ; Previous portal_unlock_channels | — | — | CostCurrency=GoldMana | — | T7Farm.cs:167 |

```csharp
35: TechNodeHelper.AddDefaultUpgrades("Farm", hasEquipment: false, hasEnhancements: false, multiWorkerAllowed: true, "FarmArtisan");
36: TechNode.Get("farm_automation_2").CostCurrency = CurrencyCollection.GoldCrown;
37: TechNode.Get("farm_automation_3").CostCurrency = CurrencyCollection.GoldCrown;
38: TechNode.Get("farm_quality").CostCurrency = CurrencyCollection.GoldCrown;
39: TechNode.Get("farm_productivity").CostCurrency = CurrencyCollection.GoldCrown;
```

## Kitchen branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| kitchen | FlowElement | ; Previous farm | — | — | CostMultiplier=4.0 | — | T7Kitchen.cs:10 |
| hamburger | Recipe | Root kitchen;  | butcher_cattle | — | Inherited/default | — | T7Kitchen.cs:24 |
| salamander_skewer | Recipe | Root kitchen;  | butcher_salamander | — | Inherited/default | — | T7Kitchen.cs:31 |
| stalker_stew | Recipe | Root kitchen;  | butcher_stalker | — | Inherited/default | — | T7Kitchen.cs:38 |
| restaurant | FlowElement | ; Previous kitchen | — | — | CostMultiplier=4.0 | — | T7Kitchen.cs:45 |
| restaurant_big_tippers | UpgradeSlot | ; Previous restaurant_automation | — | — | Inherited/default | — | T7Kitchen.cs:57 |
| restaurant_crowns | UpgradeSlot | ; Previous restaurant_automation | — | — | Inherited/default | — | T7Kitchen.cs:68 |
| pantry | FlowElement | ; Previous restaurant | — | — | CostCurrency=GoldCrown; CostMultiplier=2.0 | — | T7Kitchen.cs:79 |
| pantry_unlock_channels | Utility | ; Previous pantry | portal | Always hidden | CostCurrency=GoldMana; CostMultiplier=2.0 | — | T7Kitchen.cs:88 |
| luxury_shop | FlowElement | ; Previous restaurant | — | — | CostCurrency=GoldCrown; CostMultiplier=5.0 | — | T7Kitchen.cs:99 |

```csharp
19: TechNodeHelper.AddDefaultUpgrades("Kitchen");
20: TechNode.Get("kitchen_automation_2").CostCurrency = CurrencyCollection.GoldCrown;
21: TechNode.Get("kitchen_automation_3").CostCurrency = CurrencyCollection.GoldCrown;
22: TechNode.Get("kitchen_quality").CostCurrency = CurrencyCollection.GoldCrown;
23: TechNode.Get("kitchen_productivity").CostCurrency = CurrencyCollection.GoldCrown;
54: TechNode.Add(TechNodeHelper.UpgradeWorker("Restaurant"));
55: TechNode.Add(TechNodeHelper.UpgradeSlot2("Restaurant")).CostCurrency = CurrencyCollection.GoldCrown;
56: TechNode.Add(TechNodeHelper.UpgradeSlot3("Restaurant")).CostCurrency = CurrencyCollection.GoldCrown;
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T7Butcher.cs:10`
- `Assets.Source.Player.Tech/T7Butcher.cs:28`
- `Assets.Source.Player.Tech/T7Butcher.cs:34`
- `Assets.Source.Player.Tech/T7Butcher.cs:40`
- `Assets.Source.Player.Tech/T7Butcher.cs:46`
- `Assets.Source.Player.Tech/T7Farm.cs:15`
- `Assets.Source.Player.Tech/T7Farm.cs:40`
- `Assets.Source.Player.Tech/T7Farm.cs:50`
- `Assets.Source.Player.Tech/T7Farm.cs:60`
- `Assets.Source.Player.Tech/T7Farm.cs:70`
- `Assets.Source.Player.Tech/T7Farm.cs:81`
- `Assets.Source.Player.Tech/T7Farm.cs:92`
- `Assets.Source.Player.Tech/T7Farm.cs:102`
- `Assets.Source.Player.Tech/T7Farm.cs:113`
- `Assets.Source.Player.Tech/T7Farm.cs:125`
- `Assets.Source.Player.Tech/T7Farm.cs:133`
- `Assets.Source.Player.Tech/T7Farm.cs:141`
- `Assets.Source.Player.Tech/T7Farm.cs:151`
- `Assets.Source.Player.Tech/T7Farm.cs:167`
- `Assets.Source.Player.Tech/T7Kitchen.cs:10`
- `Assets.Source.Player.Tech/T7Kitchen.cs:24`
- `Assets.Source.Player.Tech/T7Kitchen.cs:31`
- `Assets.Source.Player.Tech/T7Kitchen.cs:38`
- `Assets.Source.Player.Tech/T7Kitchen.cs:45`
- `Assets.Source.Player.Tech/T7Kitchen.cs:57`
- `Assets.Source.Player.Tech/T7Kitchen.cs:68`
- `Assets.Source.Player.Tech/T7Kitchen.cs:79`
- `Assets.Source.Player.Tech/T7Kitchen.cs:88`
- `Assets.Source.Player.Tech/T7Kitchen.cs:99`
