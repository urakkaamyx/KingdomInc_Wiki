# WorldFlowDistributor — source reference

Assets.Behaviour.Flow.Elements/WorldFlowDistributor.cs · 86 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class WorldFlowDistributor : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, ITooltipTitleSource, ITooltipCustomSource |
| 39 | public void UpdateTooltip() |
| 49 | public void AddOutputSlot() |
| 65 | public void OnPointerEnter(PointerEventData eventData) |
| 71 | public void OnPointerExit(PointerEventData eventData) |
| 77 | public string GetTooltipTitle() |
| 82 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Production status, routing buttons, and recent results](production-status-and-controls.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowDistributor.cs:1`
