# InventoryItem — source reference

Assets.Source.Items/InventoryItem.cs · 172 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class InventoryItem : IJsonSource |
| 11 | public readonly ItemData Data |
| 15 | public ItemType Type { get; private set; } |
| 17 | public float Quality { get; private set; } = 1f |
| 19 | public string DisplayName => Type.GetDisplayName(this) |
| 21 | public string Description => Type.GetDescription(this) |
| 23 | public Sprite Icon => Type.GetIcon(this) |
| 25 | public long SellValue => Type.GetSellValue(this) |
| 27 | public int ManaValue |
| 53 | public InventoryItem(ItemType type) |
| 59 | public void ChangeItemType(ItemType t) |
| 68 | public void AddToTooltip(UITooltip tooltip) |
| 73 | public void SetQuality(float quality) |
| 83 | public void InitializeData() |
| 88 | public string GetSeed() |
| 97 | public int GetAppraiserStat(AppraiserStat stat) |
| 102 | public InventoryItem CloneItem() |
| 107 | public bool CanEnhance(EnhancementType type) |
| 116 | public string GetTypeString() |
| 130 | public JsonValue ToJson() |
| 139 | public static InventoryItem FromJson(JsonValue json) |
| 148 | public static InventoryItem FromTypeString(string itemStr) |

## Documented by

| Wiki article |
| --- |
| [Disenchanting and mana production](production-mana.md) |
| [Item quality and critical crafting](production-quality.md) |

## Sources

- `Assets.Source.Items/InventoryItem.cs:1`
