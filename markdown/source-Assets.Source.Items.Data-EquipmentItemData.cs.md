# EquipmentItemData — source reference

Assets.Source.Items.Data/EquipmentItemData.cs · 180 lines · 6 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class EquipmentItemData : ItemData |
| 15 | public readonly StatSet Stats |
| 19 | public IEnumerable<ItemEnhancementData> Enhancements |
| 33 | public EquipmentItemData(InventoryItem item) |
| 44 | public int GetStat(EquipStat s) |
| 57 | public override void UpdateQuality() |
| 67 | public override void SetMinimumRolls() |
| 77 | public override void SetMaximumRolls() |
| 87 | public (int min, int max) GetRollRange(EquipStat stat) |
| 93 | public bool HasEnhancement() |
| 105 | public bool CanEnhance(EnhancementType type) |
| 121 | public bool HasEnhancement(EnhancementType type) |
| 126 | public ItemEnhancementData GetEnhancement(EnhancementType type) |
| 131 | public void AddEnhancement(ItemEnhancementData enh) |
| 149 | public override void DataToJson(JsonObject data) |
| 167 | public override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Full Enhance](achievement-FullEnhance.md) |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |
| [Equipment slots, hands, and armor affinity](equipment-slots-and-hands.md) |
| [Enchanting, engraving, and blessings](production-enhancements.md) |
| [Item quality and critical crafting](production-quality.md) |
| [Refining and destruction risk](production-refining.md) |

## Sources

- `Assets.Source.Items.Data/EquipmentItemData.cs:1`
