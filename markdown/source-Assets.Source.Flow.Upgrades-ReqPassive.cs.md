# ReqPassive — source reference

Assets.Source.Flow.Upgrades/ReqPassive.cs · 32 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class ReqPassive : FlowUpgrade |
| 8 | public const float ProfitPerTick = 0.02f |
| 10 | public const float TickTime = 1f |
| 12 | public override string DisplayName => "@req_passive" |
| 14 | public override string IconName => "Icons_124" |
| 16 | public override int MinCostTier => 3 |
| 18 | public override double CostMultiplier => 1.5 |
| 20 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 25 | protected override void DataToJson(JsonObject data) |
| 29 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Bureaucrat](upgrade-ReqPassive.md) |

## Sources

- `Assets.Source.Flow.Upgrades/ReqPassive.cs:1`
