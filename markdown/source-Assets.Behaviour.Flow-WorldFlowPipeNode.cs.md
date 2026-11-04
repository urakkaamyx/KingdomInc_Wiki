# WorldFlowPipeNode — source reference

Assets.Behaviour.Flow/WorldFlowPipeNode.cs · 168 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class WorldFlowPipeNode : MonoBehaviour, IDragDropTarget, IPointerClickHandler, IEventSystemHandler, IBeginDragHandler, IDragHandler, IPointerEnterHandler, IPointerExitHandler, IPointerDownHandler |
| 29 | public Vector2Int Position => _pipe.Pipe.Nodes[_nodeIndex] |
| 36 | public void SetPipeNode(WorldFlowPipe pipe, int idx) |
| 42 | public void UpdatePosition(Vector2Int pos, bool updateModel = false, bool updateLine = false) |
| 55 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |
| 66 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 71 | public void OnDragDropEnd() |
| 77 | public void OnDragDropCancel() |
| 95 | public void OnPointerClick(PointerEventData eventData) |
| 107 | public void RemoveNode() |
| 112 | public void OnBeginDrag(PointerEventData eventData) |
| 120 | public void OnDrag(PointerEventData eventData) |
| 124 | public void StartDragDrop(bool hold) |
| 136 | public void OnPointerEnter(PointerEventData eventData) |
| 142 | public void OnPointerExit(PointerEventData eventData) |
| 151 | public void OnPointerDown(PointerEventData eventData) |
| 164 | public static Vector2Int ClampToGrid(Vector2Int pos) |

## Documented by

| Wiki article |
| --- |
| [Deconstruction and refunds](deconstruction-and-refunds.md) |
| [Pipes, waypoints, and port inspection](pipe-editing-and-port-inspection.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowPipeNode.cs:1`
