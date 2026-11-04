# FragmentedNightmareReward — source reference

Assets.Source.Adventure.Rewards/FragmentedNightmareReward.cs · 64 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class FragmentedNightmareReward : ItemReward |
| 10 | public bool Ready |
| 22 | public override Sprite Icon => SpriteLibrary.Get(Ready ? "Icons3_88" : "Icons3_100") |
| 24 | public override string Description |
| 36 | public FragmentedNightmareReward() |
| 41 | public override void DoReward(QuestProgress q, QuestBoard where) |
| 45 | public override void DoReward(DungeonProgress d, Dungeon where) |
| 53 | public override void AddToTooltip(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Nightmare adventure scaling and final rewards](nightmare-adventure-scaling.md) |
| [Nightmares and the endgame loop](nightmare-loop.md) |

## Sources

- `Assets.Source.Adventure.Rewards/FragmentedNightmareReward.cs:1`
