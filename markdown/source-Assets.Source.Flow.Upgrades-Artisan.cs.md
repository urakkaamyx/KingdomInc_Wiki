# Artisan — source reference

Assets.Source.Flow.Upgrades/Artisan.cs · 45 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class Artisan : FlowUpgrade |
| 9 | public const float ResourceAddedCost = 0.2f |
| 11 | public const float CraftingAddedCost = 0.1f |
| 13 | public const float QualityBonus = 0.1f |
| 15 | public override string DisplayName => "@artisan" |
| 17 | public override string IconName => "Icons_118" |
| 19 | public override int MinCostTier => 4 |
| 21 | public override double CostMultiplier => 2.0 |
| 23 | public override bool IsAvailableFor(FlowElement flowElement) |
| 28 | public override float GetQualityBonus(FlowElement forElement, int nthUpgrade) |
| 33 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 38 | protected override void DataToJson(JsonObject data) |
| 42 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Workers, upgrades, stacking, and refunds](production-upgrades.md) |
| [Artisan](upgrade-Artisan.md) |

## Sources

- `Assets.Source.Flow.Upgrades/Artisan.cs:1`
