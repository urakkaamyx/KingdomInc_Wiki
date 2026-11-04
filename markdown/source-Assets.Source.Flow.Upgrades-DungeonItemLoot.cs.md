# DungeonItemLoot — source reference

Assets.Source.Flow.Upgrades/DungeonItemLoot.cs · 32 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class DungeonItemLoot : FlowUpgrade |
| 7 | public override string DisplayName => "@dungeon_item_loot" |
| 9 | public override string IconName => "Icons_118" |
| 11 | public override int MinCostTier => 2 |
| 13 | public override double CostMultiplier => 1.5 |
| 15 | public override float GetQualityBonus(FlowElement forElement, int nthUpgrade) |
| 20 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 25 | protected override void DataToJson(JsonObject data) |
| 29 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Quest challenges, rewards, and permanent discounts](quest-challenges-and-rewards.md) |
| [Perfectly Preserved](upgrade-DungeonItemLoot.md) |

## Sources

- `Assets.Source.Flow.Upgrades/DungeonItemLoot.cs:1`
