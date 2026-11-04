# WorldFlowIO — source reference

Assets.Behaviour.Flow/WorldFlowIO.cs · 444 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 18 | public class WorldFlowIO : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, IDragDropTarget, IPointerClickHandler, IBeginDragHandler, IDragHandler, ITooltipTitleSource, ITooltipCustomSource |
| 68 | public FlowIO IO { get; private set; } |
| 83 | public void SetIO(FlowIO io) |
| 139 | public void OnPointerClick(PointerEventData eventData) |
| 156 | public void OnBeginDrag(PointerEventData eventData) |
| 164 | public void OnDrag(PointerEventData eventData) |
| 203 | public void OnDragDropMove(Vector2Int mousePosition, Vector2Int grabOffset) |
| 213 | public void OnDragDropCancel() |
| 220 | public Vector2Int GetGrabOffset(Vector2Int mousePosition) |
| 225 | public void OnDragDropEnd() |
| 321 | public void OnPointerEnter(PointerEventData eventData) |
| 361 | public void OnPointerExit(PointerEventData eventData) |
| 413 | public string GetTooltipTitle() |
| 428 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Pipes, waypoints, and port inspection](pipe-editing-and-port-inspection.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowIO.cs:1`
