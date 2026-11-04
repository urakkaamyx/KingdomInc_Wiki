# WarStage — source reference

Assets.Source.Adventure/WarStage.cs · 38 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class WarStage |
| 9 | public string DisplayName |
| 11 | public string Description |
| 13 | public string RewardDescription |
| 15 | public string RewardComplete |
| 17 | public string IconName |
| 19 | public string NotifyCompleteText = "@WarSecuredNotification" |
| 21 | public string NotifyCompleteIconName |
| 23 | public Action OnComplete |
| 25 | public int ProgressAmount |
| 27 | public int EnemyDamage |
| 29 | public int StartStrength |
| 31 | public int EndStrength |
| 33 | public Sprite Icon => SpriteLibrary.Get(IconName) |
| 35 | public Sprite NotifyCompleteIcon => SpriteLibrary.Get(NotifyCompleteIconName ?? IconName) |
| 37 | public bool Unlocked => GamePlayer.Current.HasWarStage(this) |

## Documented by

| Wiki article |
| --- |
| [War selection and status panels](war-panel-controls.md) |

## Sources

- `Assets.Source.Adventure/WarStage.cs:1`
