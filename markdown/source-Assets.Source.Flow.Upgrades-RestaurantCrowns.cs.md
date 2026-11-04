# RestaurantCrowns — source reference

Assets.Source.Flow.Upgrades/RestaurantCrowns.cs · 29 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class RestaurantCrowns : FlowUpgrade |
| 7 | public const float CrownChance = 0.1f |
| 9 | public override string DisplayName => "@restaurant_crowns" |
| 11 | public override string IconName => "Icons_188" |
| 13 | public override int MinCostTier => 2 |
| 15 | public override double CostMultiplier => 1.5 |
| 17 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 22 | protected override void DataToJson(JsonObject data) |
| 26 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Royal Assent](upgrade-RestaurantCrowns.md) |

## Sources

- `Assets.Source.Flow.Upgrades/RestaurantCrowns.cs:1`
