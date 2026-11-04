# ItemData — source reference

Assets.Source.Items/ItemData.cs · 51 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public abstract class ItemData |
| 7 | public readonly InventoryItem Item |
| 9 | public ItemData(InventoryItem item) |
| 14 | public virtual void Initialize() |
| 18 | public virtual void UpdateQuality() |
| 22 | public virtual void SetMinimumRolls() |
| 26 | public virtual void SetMaximumRolls() |
| 30 | public abstract void DataToJson(JsonObject data) |
| 32 | public abstract void DataFromJson(JsonObject data) |
| 34 | public JsonObject ToJson() |
| 45 | public static InventoryItem FromJson(JsonObject json) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Items/ItemData.cs:1`
