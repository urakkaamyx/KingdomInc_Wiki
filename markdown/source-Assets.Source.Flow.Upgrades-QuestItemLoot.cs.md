# QuestItemLoot — source reference

Assets.Source.Flow.Upgrades/QuestItemLoot.cs · 35 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class QuestItemLoot : FlowUpgrade |
| 8 | public const float QualityBonus = 0.1f |
| 10 | public override string DisplayName => "@quest_board_quality" |
| 12 | public override string IconName => "Icons_118" |
| 14 | public override int MinCostTier => 2 |
| 16 | public override double CostMultiplier => 1.5 |
| 18 | public override float GetQualityBonus(FlowElement forElement, int nthUpgrade) |
| 23 | public override string GetDescription(FlowElement forElement, int nthUpgrade) |
| 28 | protected override void DataToJson(JsonObject data) |
| 32 | protected override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Quest challenges, rewards, and permanent discounts](quest-challenges-and-rewards.md) |
| [Explorer](upgrade-QuestItemLoot.md) |

## Sources

- `Assets.Source.Flow.Upgrades/QuestItemLoot.cs:1`
