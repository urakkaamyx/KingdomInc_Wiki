# DistilledNightmareReward — source reference

Assets.Source.Adventure.Rewards/DistilledNightmareReward.cs · 78 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class DistilledNightmareReward : QuestReward |
| 14 | public bool Ready |
| 26 | public override Sprite Icon => SpriteLibrary.Get(Ready ? "Icons3_92" : "Icons3_93") |
| 28 | public override string Description |
| 40 | public override string TooltipTitle => "@distilled_nightmare" |
| 42 | public override void DoReward(QuestProgress q, QuestBoard where) |
| 46 | public override void DoReward(DungeonProgress d, Dungeon where) |
| 67 | public override void AddToTooltip(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Nightmare adventure scaling and final rewards](nightmare-adventure-scaling.md) |
| [Nightmares and the endgame loop](nightmare-loop.md) |

## Sources

- `Assets.Source.Adventure.Rewards/DistilledNightmareReward.cs:1`
