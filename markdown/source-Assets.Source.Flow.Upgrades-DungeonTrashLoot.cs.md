# DungeonTrashLoot — source reference

Assets.Source.Flow.Upgrades/DungeonTrashLoot.cs · 31 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class DungeonTrashLoot : FlowUpgrade |
| 7 | public const float RewardChance = 0.05f |
| 9 | public const float RewardAmount = 0.25f |
| 11 | public override string DisplayName => "@dungeon_trash_loot" |
| 13 | public override string IconName => "Icons_197" |
| 15 | public override int MinCostTier => 2 |
| 17 | public override double CostMultiplier => 1.5 |
| 19 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 24 | protected override void DataToJson(JsonObject data) |
| 28 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Trash Loot](upgrade-DungeonTrashLoot.md) |

## Sources

- `Assets.Source.Flow.Upgrades/DungeonTrashLoot.cs:1`
