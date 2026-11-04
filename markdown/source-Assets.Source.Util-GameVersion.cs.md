# GameVersion — source reference

Assets.Source.Util/GameVersion.cs · 69 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class GameVersion |
| 7 | public static GameVersion Loading |
| 9 | public int Major |
| 11 | public int Minor |
| 13 | public int Patch |
| 15 | public GameVersion() |
| 19 | public GameVersion(int major, int minor, int patch) |
| 26 | public bool TryParse(string vStr) |
| 39 | public bool IsBefore(int major, int minor, int patch) |
| 60 | public static GameVersion Parse(string vStr) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Util/GameVersion.cs:1`
