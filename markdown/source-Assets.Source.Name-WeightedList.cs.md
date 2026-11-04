# WeightedList — source reference

Assets.Source.Name/WeightedList.cs · 49 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class WeightedList<T> |
| 10 | public List<WeightedOption<T>> Options = new List<WeightedOption<T>>() |
| 12 | public WeightedList() |
| 16 | public WeightedList(params WeightedOption<T>[] options) |
| 21 | public T Pick(SeededRandom random) |
| 45 | public void Add(T value, int weight = 1) |

## Documented by

| Wiki article |
| --- |
| [Character names and random generation](names-and-randomness.md) |

## Sources

- `Assets.Source.Name/WeightedList.cs:1`
