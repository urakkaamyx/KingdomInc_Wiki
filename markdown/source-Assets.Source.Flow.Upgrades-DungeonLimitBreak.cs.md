# DungeonLimitBreak — source reference

Assets.Source.Flow.Upgrades/DungeonLimitBreak.cs · 36 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class DungeonLimitBreak : FlowUpgrade |
| 7 | public override string DisplayName => "@dungeon_limit_break" |
| 9 | public override string IconName => "Icons2_49" |
| 11 | public override int MinCostTier => 2 |
| 13 | public override double CostMultiplier => 2.0 |
| 15 | public override bool IsAvailableFor(FlowElement flowElement) |
| 24 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 29 | protected override void DataToJson(JsonObject data) |
| 33 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Together As One](upgrade-DungeonLimitBreak.md) |

## Sources

- `Assets.Source.Flow.Upgrades/DungeonLimitBreak.cs:1`
