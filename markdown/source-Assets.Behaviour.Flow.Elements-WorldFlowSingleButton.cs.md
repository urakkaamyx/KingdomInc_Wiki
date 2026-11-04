# WorldFlowSingleButton — source reference

Assets.Behaviour.Flow.Elements/WorldFlowSingleButton.cs · 125 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class WorldFlowSingleButton : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, IPointerClickHandler, ITooltipTitleSource, ITooltipCustomSource |
| 96 | public void OnPointerClick(PointerEventData eventData) |
| 105 | public void OnPointerEnter(PointerEventData eventData) |
| 110 | public void OnPointerExit(PointerEventData eventData) |
| 116 | public string GetTooltipTitle() |
| 121 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Track switches, timers, and release buttons](production-gates.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowSingleButton.cs:1`
