# ArenaCashier — source reference

Assets.Source.Flow.Upgrades/ArenaCashier.cs · 28 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class ArenaCashier : FlowUpgrade |
| 8 | public const float ProfitBonus = 0.1f |
| 10 | public override string DisplayName => "@arena_cashier" |
| 12 | public override string IconName => "Icons_119" |
| 14 | public override double CostMultiplier => 1.5 |
| 16 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 21 | protected override void DataToJson(JsonObject data) |
| 25 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Fight Purse](upgrade-ArenaCashier.md) |

## Sources

- `Assets.Source.Flow.Upgrades/ArenaCashier.cs:1`
