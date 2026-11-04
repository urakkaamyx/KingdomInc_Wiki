# ArmoryContents — source reference

Assets.Source.Items/ArmoryContents.cs · 161 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class ArmoryContents : IJsonSource |
| 10 | public const int ChannelCount = 8 |
| 16 | public static Color[] ChannelColor { get; private set; } = new Color[8] |
| 28 | public int GetItemCount(int channel, ItemType type) |
| 33 | public bool HasItem(int channel, ItemType type) |
| 38 | public bool CanAddTo(int channel, ItemType type, int max) |
| 43 | public IEnumerable<ItemType> GetAvailableItemTypes(int channel) |
| 54 | public void AddItem(int channel, InventoryItem item) |
| 79 | public void AddRange(int channel, IEnumerable<InventoryItem> items) |
| 87 | public InventoryItem ConsumeItem(Armory requester, int channel, ItemType type) |
| 106 | public InventoryItem PeekItem(int channel, ItemType type) |
| 126 | public JsonValue ToJson() |
| 144 | public void FromJson(JsonValue data) |

## Documented by

| Wiki article |
| --- |
| [Armories and shared item storage](production-global-storage.md) |

## Sources

- `Assets.Source.Items/ArmoryContents.cs:1`
