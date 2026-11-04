# SteamStat — source reference

Assets.Source.Player/SteamStat.cs · 75 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class SteamStat |
| 8 | public const float UpdateInterval = 1f |
| 10 | protected int _savedAmount |
| 12 | protected int _addedAmount |
| 14 | protected int _setAmount |
| 18 | public SteamStatType Stat { get; private set; } |
| 20 | public string StatName { get; private set; } |
| 22 | public int[] Tiers { get; private set; } |
| 24 | public SteamStat(SteamStatType type, int[] tiers) |
| 31 | public void Add(int count) |
| 36 | public void Set(int count) |
| 44 | public void Update(float delta) |

## Documented by

| Wiki article |
| --- |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |

## Sources

- `Assets.Source.Player/SteamStat.cs:1`
