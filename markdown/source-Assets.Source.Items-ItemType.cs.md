# ItemType — source reference

Assets.Source.Items/ItemType.cs · 376 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 15 | public class ItemType |
| 21 | public readonly string Identifier |
| 23 | public string IconName |
| 25 | public string OverrideRecipe |
| 29 | public bool SourceQuest |
| 31 | public bool SourceDungeon |
| 33 | public bool SourceArena |
| 35 | public bool SourceTraining |
| 39 | public bool CanSell = true |
| 41 | public long OverrideValue |
| 45 | public static IReadOnlyList<ItemType> All => _orderedItems |
| 47 | public static int Count => _orderedItems.Count |
| 49 | public static IEnumerable<ItemType> Unlocked |
| 63 | public int Ordinal { get; private set; } |
| 65 | public string DisplayName { private get; set; } |
| 67 | public string Description { private get; set; } |
| 69 | public CraftingRecipe DefaultRecipe |
| 95 | public virtual long BaseValue |
| 120 | public virtual bool IsUnlocked |
| 162 | protected virtual bool _addQualityToTooltip => true |
| 164 | public InventoryItem PreviewItem |
| 196 | public ItemType(string id) |
| 203 | public virtual string GetDisplayName(InventoryItem ii = null) |
| 208 | public virtual string GetDescription(InventoryItem ii = null) |
| 213 | public virtual Sprite GetIcon(InventoryItem ii = null) |
| 218 | public List<string> GetItemSources() |
| 252 | public virtual void AddToTooltip(InventoryItem item, UITooltip tooltip) |
| 270 | protected virtual void _addSourceToTooltip(InventoryItem item, UITooltip tooltip) |
| 287 | public virtual ItemData CreateItemData(InventoryItem item) |
| 292 | public virtual long GetSellValue(InventoryItem item) |
| 297 | public virtual int GetAppraiserStat(InventoryItem item, AppraiserStat stat) |
| 306 | public IEnumerable<DungeonType> GetSourceDungeons() |
| 328 | public IEnumerable<Quest> GetSourceQuests() |
| 346 | public static void Add(ItemType it) |
| 353 | public static ItemType Get(string id) |
| 358 | public static ItemType GetById(int id) |
| 363 | public static implicit operator ItemType(string id) |
| 368 | public static bool IsCraftable(ItemType it) |

## Documented by

| Wiki article |
| --- |
| [Filters, Appraisers, Inspectors, and Accountants](production-filters.md) |
| [Item quality and critical crafting](production-quality.md) |

## Sources

- `Assets.Source.Items/ItemType.cs:1`
