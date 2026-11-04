# WorldFlowDecoResizer — source reference

Assets.Behaviour.Flow/WorldFlowDecoResizer.cs · 160 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class WorldFlowDecoResizer : MonoBehaviour, IDragDropTarget, IPointerClickHandler, IEventSystemHandler, IBeginDragHandler, IDragHandler, IPointerEnterHandler, IPointerExitHandler, IPointerDownHandler |
| 36 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |
| 49 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 54 | public void OnDragDropEnd() |
| 70 | public void OnDragDropCancel() |
| 84 | public void OnPointerClick(PointerEventData eventData) |
| 92 | public void OnBeginDrag(PointerEventData eventData) |
| 100 | public void OnDrag(PointerEventData eventData) |
| 104 | public void StartDragDrop(bool hold) |
| 140 | public void OnPointerEnter(PointerEventData eventData) |
| 148 | public void OnPointerExit(PointerEventData eventData) |
| 156 | public void OnPointerDown(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Container anchors, resizing, and group movement](container-moving-and-resizing.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowDecoResizer.cs:1`
