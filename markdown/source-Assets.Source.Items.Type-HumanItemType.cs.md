# HumanItemType — source reference

Assets.Source.Items.Type/HumanItemType.cs · 217 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class HumanItemType : CombatantItemType |
| 16 | public static Dictionary<EquipmentSlot, string> TooltipSlots = new Dictionary<EquipmentSlot, string> |
| 52 | public static string MainHandEmpty = "Icons_109" |
| 54 | public static string OffHandEmpty = "Icons_133" |
| 56 | public EquipStat? PowerStat |
| 58 | public AdventurerArchetype Archetype |
| 60 | public List<AdventurerAdvancement> Advancements |
| 62 | public Func<InventoryItem, bool> EquipmentAllowed |
| 64 | public string PowerSource |
| 80 | public HumanItemType(string id) |
| 85 | public override int GetAppraiserStat(InventoryItem item, AppraiserStat stat) |
| 109 | public override long GetSellValue(InventoryItem item) |
| 120 | public bool CanEquipItem(InventoryItem item) |
| 133 | public override ItemData CreateItemData(InventoryItem item) |
| 138 | public override void AddToTooltip(InventoryItem item, UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Equipment slots, hands, and armor affinity](equipment-slots-and-hands.md) |
| [Barracks, Adventurers Guilds, and mercenaries](production-recruitment.md) |

## Sources

- `Assets.Source.Items.Type/HumanItemType.cs:1`
