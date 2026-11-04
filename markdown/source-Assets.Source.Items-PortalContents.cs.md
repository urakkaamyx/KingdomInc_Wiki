# PortalContents — source reference

Assets.Source.Items/PortalContents.cs · 150 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class PortalContents : IJsonSource |
| 10 | public const int ChannelCount = 8 |
| 12 | public const int IndexCount = 8 |
| 18 | public int MaxItemCount => 20 |
| 20 | public int GetItemCount(int channel, int index) |
| 29 | public bool HasItem(int channel, int index) |
| 34 | public bool CanAddTo(int channel, int index) |
| 39 | public void AddItem(int channel, int index, InventoryItem item) |
| 65 | public InventoryItem ConsumeItem(Portal requester, int channel, int idx) |
| 83 | public InventoryItem PeekItem(int channel, int idx) |
| 114 | public JsonValue ToJson() |
| 134 | public void FromJson(JsonValue data) |

## Documented by

| Wiki article |
| --- |
| [Portals and shared channels](production-portals.md) |

## Sources

- `Assets.Source.Items/PortalContents.cs:1`
