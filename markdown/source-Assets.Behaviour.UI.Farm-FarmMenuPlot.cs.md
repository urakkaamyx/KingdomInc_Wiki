# FarmMenuPlot — source reference

Assets.Behaviour.UI.Farm/FarmMenuPlot.cs · 85 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class FarmMenuPlot : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler |
| 32 | public void SetItem(int x, int y, FarmItemType i) |
| 56 | public string GetTooltipTitle() |
| 61 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 67 | public void UpdateItem(FarmItemType item) |
| 73 | public void OnPointerClick(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Farm plots and planting controls](farm-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Farm/FarmMenuPlot.cs:1`
