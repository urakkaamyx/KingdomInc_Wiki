# DecoSticker — source reference

Assets.Source.Flow/DecoSticker.cs · 44 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public abstract class DecoSticker : IJsonSource |
| 10 | public string Type => GetType().Name |
| 12 | public abstract CurrencyCollection GetCost() |
| 14 | public abstract Sprite GetSprite() |
| 16 | public abstract void DataToJson(JsonObject data) |
| 18 | public abstract void DataFromJson(JsonObject data) |
| 20 | public virtual DecoSticker CreateCopy() |
| 25 | public JsonValue ToJson() |
| 33 | public static DecoSticker FromJson(JsonObject data) |
| 40 | public static DecoSticker Create(string name) |

## Documented by

| Wiki article |
| --- |
| [Decorations, labels, colors, and stickers](decoration-labels-stickers.md) |

## Sources

- `Assets.Source.Flow/DecoSticker.cs:1`
