# Cashier — source reference

Assets.Source.Flow.Upgrades/Cashier.cs · 30 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class Cashier : FlowUpgrade |
| 8 | public const float ProfitBonus = 0.05f |
| 10 | public override string DisplayName => "@cashier" |
| 12 | public override string IconName => "Icons_119" |
| 14 | public override int MinCostTier => 1 |
| 16 | public override double CostMultiplier => 1.5 |
| 18 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 23 | protected override void DataToJson(JsonObject data) |
| 27 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Cashier](upgrade-Cashier.md) |

## Sources

- `Assets.Source.Flow.Upgrades/Cashier.cs:1`
