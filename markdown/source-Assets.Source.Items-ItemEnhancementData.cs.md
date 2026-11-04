# ItemEnhancementData — source reference

Assets.Source.Items/ItemEnhancementData.cs · 50 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class ItemEnhancementData : IJsonSource |
| 9 | public readonly ItemEnhancement Enhancement |
| 11 | public float Quality = 1f |
| 13 | public string TextLine => Enhancement.GetTextLine(Quality) |
| 15 | public long SellValue => (long)Math.Round((float)Enhancement.BaseValue * Quality) |
| 17 | public ItemEnhancementData(ItemEnhancement enhancement) |
| 22 | public int GetStat(EquipStat stat) |
| 27 | public JsonValue ToJson() |
| 37 | public static ItemEnhancementData FromJson(JsonValue json) |

## Documented by

| Wiki article |
| --- |
| [Equipment slots, hands, and armor affinity](equipment-slots-and-hands.md) |

## Sources

- `Assets.Source.Items/ItemEnhancementData.cs:1`
