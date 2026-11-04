# CurrencyReward — source reference

Assets.Source.Adventure.Rewards/CurrencyReward.cs · 43 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class CurrencyReward : QuestReward |
| 12 | public readonly Currency Currency |
| 14 | public readonly int Count |
| 16 | public override Sprite Icon => Currency.GetIcon() |
| 18 | public override string Description => Translation.Translate("#{0}# {1}", Count, Currency.GetDisplayName()) |
| 20 | public CurrencyReward(Currency c, int count) |
| 26 | public override void DoReward(QuestProgress q, QuestBoard where) |
| 31 | public override void DoReward(DungeonProgress d, Dungeon where) |
| 36 | public void DoReward(FlowElement where, float rewardMultiplier = 1f) |

## Documented by

| Wiki article |
| --- |
| [Dungeon runs, stages, loot, and retreat](dungeon-run-mechanics.md) |
| [Quest challenges, rewards, and permanent discounts](quest-challenges-and-rewards.md) |

## Sources

- `Assets.Source.Adventure.Rewards/CurrencyReward.cs:1`
