# CultureProfile — source reference

Assets.Source.Name/CultureProfile.cs · 39 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class CultureProfile |
| 8 | public string CultureId |
| 10 | public string DisplayName |
| 12 | public int CultureWeight = 1 |
| 14 | public int MinGivenSyllables = 2 |
| 16 | public int MaxGivenSyllables = 3 |
| 18 | public int MinSurnameSyllables = 2 |
| 20 | public int MaxSurnameSyllables = 3 |
| 22 | public WeightedList<string> GivenStarts = new WeightedList<string>() |
| 24 | public WeightedList<string> GivenMiddles = new WeightedList<string>() |
| 26 | public WeightedList<string> GivenEnds = new WeightedList<string>() |
| 28 | public WeightedList<string> SurnameStarts = new WeightedList<string>() |
| 30 | public WeightedList<string> SurnameMiddles = new WeightedList<string>() |
| 32 | public WeightedList<string> SurnameEnds = new WeightedList<string>() |
| 34 | public WeightedList<string> FixedSurnames = new WeightedList<string>() |
| 36 | public WeightedList<string> PlaceNames = new WeightedList<string>() |
| 38 | public WeightedList<SurnamePattern> SurnamePatterns = new WeightedList<SurnamePattern>() |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Name/CultureProfile.cs:1`
