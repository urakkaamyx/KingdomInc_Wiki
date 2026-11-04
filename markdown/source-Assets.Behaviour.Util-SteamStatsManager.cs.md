# SteamStatsManager — source reference

Assets.Behaviour.Util/SteamStatsManager.cs · 123 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class SteamStatsManager : MonoBehaviour |
| 11 | public const float StatsStoreInterval = 300f |
| 43 | public void OnGameOverlayActivated(GameOverlayActivated_t data) |
| 94 | public static void Init() |
| 102 | public static int Get(SteamStatType type) |
| 108 | public static void Add(SteamStatType type, int count) |
| 116 | public static void Set(SteamStatType type, int val) |

## Documented by

| Wiki article |
| --- |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |
| [Saves, autosaves, pause, and offline behavior](saves-time-and-offline.md) |

## Sources

- `Assets.Behaviour.Util/SteamStatsManager.cs:1`
