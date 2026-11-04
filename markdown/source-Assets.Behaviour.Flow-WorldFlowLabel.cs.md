# WorldFlowLabel — source reference

Assets.Behaviour.Flow/WorldFlowLabel.cs · 119 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class WorldFlowLabel : MonoBehaviour, IDragDropTarget, IPointerClickHandler, IEventSystemHandler, IBeginDragHandler, IDragHandler |
| 23 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |
| 33 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 39 | public void OnDragDropEnd() |
| 56 | public void OnDragDropCancel() |
| 67 | public void SwapToFlow(int fromFlow, int toFlow) |
| 80 | public void OnPointerClick(PointerEventData eventData) |
| 96 | public void OnBeginDrag(PointerEventData eventData) |
| 104 | public void OnDrag(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Map navigation and dragging](map-navigation-and-dragging.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowLabel.cs:1`
