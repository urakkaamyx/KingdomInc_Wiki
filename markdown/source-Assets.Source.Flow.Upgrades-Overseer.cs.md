# Overseer — source reference

Assets.Source.Flow.Upgrades/Overseer.cs · 50 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class Overseer : FlowUpgrade |
| 9 | public const float ProductivityBonus = 0.1f |
| 11 | public override string DisplayName => "@overseer" |
| 13 | public override string IconName => "Icons2_76" |
| 15 | public override int MinCostTier => 4 |
| 17 | public override double CostMultiplier => 1.5 |
| 19 | public override bool IsAvailableFor(FlowElement flowElement) |
| 24 | public override float GetProductivityBonus(FlowElement forElement, int nthUpgrade) |
| 29 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 43 | protected override void DataToJson(JsonObject data) |
| 47 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Productivity and handcrafting](production-productivity.md) |
| [Overseer](upgrade-Overseer.md) |

## Sources

- `Assets.Source.Flow.Upgrades/Overseer.cs:1`
