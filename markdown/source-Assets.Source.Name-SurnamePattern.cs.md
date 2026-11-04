# SurnamePattern — source reference

Assets.Source.Name/SurnamePattern.cs · 42 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class SurnamePattern |
| 9 | public SurnamePatternType Type |
| 11 | public int Weight = 1 |
| 13 | public string Prefix |
| 15 | public string Connector |
| 17 | public string Suffix |
| 19 | public SurnamePattern(SurnamePatternType type, int weight = 1) |
| 25 | public SurnamePattern WithPrefix(string prefix) |
| 31 | public SurnamePattern WithConnector(string connector) |
| 37 | public SurnamePattern WithSuffix(string suffix) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Name/SurnamePattern.cs:1`
