# WorldFlowDecoMover — source reference

Assets.Behaviour.Flow/WorldFlowDecoMover.cs · 283 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class WorldFlowDecoMover : MonoBehaviour, IDragDropTarget, IPointerClickHandler, IEventSystemHandler, IBeginDragHandler, IDragHandler, IPointerEnterHandler, IPointerExitHandler |
| 44 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |
| 79 | public void SwapToFlow(int fromFlow, int toFlow) |
| 118 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 128 | public void OnDragDropEnd() |
| 151 | public void OnDragDropCancel() |
| 197 | public void OnPointerClick(PointerEventData eventData) |
| 209 | public void OnBeginDrag(PointerEventData eventData) |
| 217 | public void OnDrag(PointerEventData eventData) |
| 221 | public void StartDragDrop(bool hold, bool isTemporary = false) |
| 263 | public void OnPointerEnter(PointerEventData eventData) |
| 271 | public void OnPointerExit(PointerEventData eventData) |
| 279 | public (IEnumerable<WorldFlowElement> elements, IEnumerable<WorldFlowDeco> decos, IEnumerable<WorldFlowPipeNode> pipeNodes) GetAnchoredParts() |

## Documented by

| Wiki article |
| --- |
| [Container anchors, resizing, and group movement](container-moving-and-resizing.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowDecoMover.cs:1`
