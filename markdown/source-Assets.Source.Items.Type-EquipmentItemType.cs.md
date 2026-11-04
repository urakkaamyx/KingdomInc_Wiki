# EquipmentItemType — source reference

Assets.Source.Items.Type/EquipmentItemType.cs · 160 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class EquipmentItemType : ResourceItemType |
| 13 | public ArmorType ArmorType |
| 15 | public StatSet BaseStats = new StatSet() |
| 17 | public AdventurerTrait EquipTrait |
| 19 | public virtual EquipmentSlot Slot { get; set; } |
| 21 | public override bool IsUnlocked |
| 33 | public EquipmentItemType(string id) |
| 38 | public override ItemData CreateItemData(InventoryItem item) |
| 43 | public override long GetSellValue(InventoryItem item) |
| 53 | public int GetStat(InventoryItem item, EquipStat stat) |
| 58 | public EquipStat GetMainStat() |
| 74 | public override int GetAppraiserStat(InventoryItem item, AppraiserStat stat) |
| 91 | public IEnumerable<ItemEnhancementData> GetEnhancements(InventoryItem item) |
| 96 | public ActiveTrait PreviewActiveTrait(InventoryItem item) |
| 101 | public override void AddToTooltip(InventoryItem item, UITooltip tooltip) |
| 144 | public virtual string GetSlotDescription() |

## Documented by

| Wiki article |
| --- |
| [Adventurer classes and advancement routes](class-progression.md) |
| [Item quality and critical crafting](production-quality.md) |

## Sources

- `Assets.Source.Items.Type/EquipmentItemType.cs:1`
