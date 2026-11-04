# WarType — source reference

Assets.Source.Adventure/WarType.cs · 82 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class WarType |
| 11 | public const float TickDelay = 2f |
| 15 | public readonly string Identifier |
| 17 | public string DisplayName |
| 19 | public string Description |
| 21 | public string IconName |
| 23 | public string EnemyIconName |
| 25 | public bool IsEndgame |
| 27 | public float MedalsMultiplier = 1f |
| 29 | public Func<bool> CanProgress = () => true |
| 31 | public string ProgressBlockedReason |
| 33 | public WarStage[] Stages |
| 35 | public Sprite Icon => SpriteLibrary.Get(IconName) |
| 37 | public Sprite EnemyIcon => SpriteLibrary.Get(EnemyIconName) |
| 39 | public WarProgress Progress => GamePlayer.Current.GetWarProgress(this) |
| 41 | public WarStage CurrentStage |
| 63 | public WarType(string id) |
| 68 | public static void Add(WarType war) |
| 73 | public static WarType Get(string id) |
| 78 | public static implicit operator WarType(string id) |

## Documented by

| Wiki article |
| --- |
| [War selection and status panels](war-panel-controls.md) |

## Sources

- `Assets.Source.Adventure/WarType.cs:1`
