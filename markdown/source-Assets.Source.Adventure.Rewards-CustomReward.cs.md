# CustomReward — source reference

Assets.Source.Adventure.Rewards/CustomReward.cs · 41 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class CustomReward : QuestReward |
| 16 | public override Sprite Icon => SpriteLibrary.Get(_iconName) |
| 18 | public override string Description => _description |
| 20 | public CustomReward(string desc, string iconName, Action<FlowElement> onReward) |
| 27 | public override void DoReward(QuestProgress q, QuestBoard where) |
| 32 | public override void DoReward(DungeonProgress d, Dungeon where) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Adventure.Rewards/CustomReward.cs:1`
