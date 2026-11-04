# GameMath — source reference

Assets.Source.Util/GameMath.cs · 108 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class GameMath |
| 9 | public const float TierScaleFactor = 2.3f |
| 11 | public static string FormatNumber(double num, int decimals = -1) |
| 53 | public static string FormatTime(int tSec, bool shortFormat = false) |
| 67 | public static string FormatPercentage(double percentage, FormatPercentageMode mode = FormatPercentageMode.Default, int decimals = 0) |
| 79 | public static bool LineIntersects(Vector2 lineOneA, Vector2 lineOneB, Vector2 lineTwoA, Vector2 lineTwoB) |
| 88 | public static long RoundGold(long gold, int maxCount = 2) |

## Documented by

| Wiki article |
| --- |
| [Technology cost formula](technology-costs.md) |

## Sources

- `Assets.Source.Util/GameMath.cs:1`
