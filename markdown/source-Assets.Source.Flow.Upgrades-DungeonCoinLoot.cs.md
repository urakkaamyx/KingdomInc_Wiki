# DungeonCoinLoot — source reference

Assets.Source.Flow.Upgrades/DungeonCoinLoot.cs · 27 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class DungeonCoinLoot : FlowUpgrade |
| 7 | public override string DisplayName => "@dungeon_coin_loot" |
| 9 | public override string IconName => "Icons_119" |
| 11 | public override int MinCostTier => 2 |
| 13 | public override double CostMultiplier => 1.5 |
| 15 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 20 | protected override void DataToJson(JsonObject data) |
| 24 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Ancient Treasures](upgrade-DungeonCoinLoot.md) |

## Sources

- `Assets.Source.Flow.Upgrades/DungeonCoinLoot.cs:1`
