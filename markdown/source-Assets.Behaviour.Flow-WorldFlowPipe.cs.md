# WorldFlowPipe — source reference

Assets.Behaviour.Flow/WorldFlowPipe.cs · 179 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class WorldFlowPipe : MonoBehaviour |
| 22 | public Vector2Int GhostConnection |
| 26 | public FlowPipe Pipe { get; private set; } |
| 28 | public IEnumerable<WorldFlowPipeNode> Nodes => _nodes |
| 36 | public void SetFlowPipe(FlowPipe pipe) |
| 44 | public void AddNewNode(Vector2Int pos) |
| 53 | public void RemoveNode(int idx) |
| 60 | public void UpdateLinePositions() |
| 102 | public void ItemTransferred(InventoryItem item) |
| 110 | public void ItemRejected(InventoryItem item) |
| 119 | public void ItemTimeout() |

## Documented by

| Wiki article |
| --- |
| [Pipes, waypoints, and port inspection](pipe-editing-and-port-inspection.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowPipe.cs:1`
