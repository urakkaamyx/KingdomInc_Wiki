# QuestReward — source reference

Assets.Source.Adventure/QuestReward.cs · 22 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public abstract class QuestReward |
| 9 | public abstract Sprite Icon { get; } |
| 11 | public abstract string Description { get; } |
| 13 | public virtual string TooltipTitle => null |
| 15 | public abstract void DoReward(QuestProgress q, QuestBoard where) |
| 17 | public abstract void DoReward(DungeonProgress d, Dungeon where) |
| 19 | public virtual void AddToTooltip(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Adventure/QuestReward.cs:1`
