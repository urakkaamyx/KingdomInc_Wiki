# FarmMenuItem — source reference

Assets.Behaviour.UI.Farm/FarmMenuItem.cs · 103 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class FarmMenuItem : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler, IBeginDragHandler, IDragHandler |
| 40 | public void SetItem(FarmItemType item) |
| 63 | public string GetTooltipTitle() |
| 68 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 75 | public void OnDrag(PointerEventData eventData) |
| 79 | public void OnBeginDrag(PointerEventData eventData) |
| 87 | public void OnPointerClick(PointerEventData eventData) |
| 95 | public void StartDragItem(bool hold) |

## Documented by

| Wiki article |
| --- |
| [Farm plots and planting controls](farm-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Farm/FarmMenuItem.cs:1`
