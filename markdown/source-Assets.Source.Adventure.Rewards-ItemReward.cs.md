# ItemReward — source reference

Assets.Source.Adventure.Rewards/ItemReward.cs · 69 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class ItemReward : QuestReward |
| 13 | public readonly ItemType Item |
| 15 | public readonly float Quality = 1f |
| 17 | public readonly int Count = 1 |
| 19 | public override Sprite Icon => Item.GetIcon() |
| 21 | public override string Description => Translation.TranslateOnly(Item.GetDisplayName()) + ((Count > 1) ? (" x" + GameMath.FormatNumber(Count)) : "") |
| 23 | public override string TooltipTitle => Item.GetDisplayName() |
| 25 | public ItemReward(ItemType item, float quality = 1f, int count = 1) |
| 32 | public override void AddToTooltip(UITooltip tooltip) |
| 37 | public override void DoReward(QuestProgress q, QuestBoard where) |
| 42 | public override void DoReward(DungeonProgress d, Dungeon where) |
| 47 | protected void _doReward(FlowElement where) |

## Documented by

| Wiki article |
| --- |
| [Quest challenges, rewards, and permanent discounts](quest-challenges-and-rewards.md) |

## Sources

- `Assets.Source.Adventure.Rewards/ItemReward.cs:1`
