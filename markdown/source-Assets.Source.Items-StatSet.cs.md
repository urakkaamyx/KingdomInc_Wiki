# StatSet — source reference

Assets.Source.Items/StatSet.cs · 81 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class StatSet : IEnumerable<(EquipStat stat, int amt)>, IEnumerable |
| 13 | public StatSet() |
| 18 | public void Clear() |
| 26 | public void Add((EquipStat stat, int amt) row) |
| 31 | public void Add(EquipStat stat, int amt) |
| 36 | public int Get(EquipStat stat) |
| 41 | public IEnumerator<(EquipStat stat, int amt)> GetEnumerator() |
| 59 | public JsonValue ToJson() |
| 73 | public void LoadFromJson(JsonObject json) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Items/StatSet.cs:1`
