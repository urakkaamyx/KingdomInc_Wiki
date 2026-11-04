# WorldFlowCollector — source reference

Assets.Behaviour.Flow.Elements/WorldFlowCollector.cs · 85 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class WorldFlowCollector : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, ITooltipTitleSource, ITooltipCustomSource |
| 39 | public void UpdateTooltip() |
| 49 | public void AddInputSlot() |
| 64 | public void OnPointerEnter(PointerEventData eventData) |
| 70 | public void OnPointerExit(PointerEventData eventData) |
| 76 | public string GetTooltipTitle() |
| 81 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Production status, routing buttons, and recent results](production-status-and-controls.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowCollector.cs:1`
