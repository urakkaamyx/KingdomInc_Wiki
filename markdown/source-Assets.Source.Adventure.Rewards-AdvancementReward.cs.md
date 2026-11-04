# AdvancementReward — source reference

Assets.Source.Adventure.Rewards/AdvancementReward.cs · 58 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class AdvancementReward : QuestReward |
| 12 | public AdventurerItemType BaseType |
| 14 | public AdventurerItemType Advancement |
| 16 | public Sprite _icon |
| 18 | public override Sprite Icon => _icon |
| 20 | public override string Description => Translation.TranslateOnly("@quest_reward_advancement", Advancement.GetDisplayName(), BaseType.GetDisplayName()) |
| 22 | public AdvancementReward(ItemType baseType, ItemType advancement) |
| 35 | public override void DoReward(QuestProgress q, QuestBoard where) |
| 43 | public override void DoReward(DungeonProgress d, Dungeon where) |

## Documented by

| Wiki article |
| --- |
| [Adventurer classes and advancement routes](class-progression.md) |

## Sources

- `Assets.Source.Adventure.Rewards/AdvancementReward.cs:1`
