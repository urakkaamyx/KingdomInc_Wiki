# FlowIO — source reference

Assets.Source.Flow/FlowIO.cs · 120 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public abstract class FlowIO : IJsonSource |
| 10 | public delegate bool FlowFilter(InventoryItem item) |
| 12 | public readonly FlowElement Parent |
| 14 | public readonly int ParentIndex |
| 16 | public int Position |
| 18 | public ItemType Item |
| 20 | public FlowFilter Filter |
| 22 | public bool FilterPreview |
| 24 | public int BufferSize |
| 26 | public List<InventoryItem> BufferedItems = new List<InventoryItem>() |
| 28 | public FlowPipe ConnectedPipe |
| 30 | public WorldFlowIO World |
| 32 | public bool CanBuffer => BufferedItems.Count < BufferSize |
| 34 | public bool HasBuffer => BufferedItems.Count > 0 |
| 36 | public InventoryItem NextItem |
| 48 | public FlowIO(FlowElement parent, int parentIndex) |
| 54 | public virtual bool CanAcceptItem(InventoryItem item) |
| 67 | public void ConsumeItem(InventoryItem item) |
| 72 | public InventoryItem ConsumeItem() |
| 83 | public List<ItemType> GetPreviewTypes() |
| 103 | public virtual JsonValue ToJson() |
| 115 | public virtual void FromJson(JsonValue json) |

## Documented by

| Wiki article |
| --- |
| [Production simulation and bottlenecks](production-simulation.md) |

## Sources

- `Assets.Source.Flow/FlowIO.cs:1`
