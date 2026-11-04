# Coffers — source reference

Assets.Source.Flow.Upgrades/Coffers.cs · 30 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class Coffers : FlowUpgrade |
| 8 | public const int StorageBonus = 2 |
| 10 | public override string DisplayName => "@coffers" |
| 12 | public override string IconName => "Icons_120" |
| 14 | public override int MinCostTier => 2 |
| 16 | public override double CostMultiplier => 1.5 |
| 18 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 23 | protected override void DataToJson(JsonObject data) |
| 27 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Coffers](upgrade-Coffers.md) |

## Sources

- `Assets.Source.Flow.Upgrades/Coffers.cs:1`
