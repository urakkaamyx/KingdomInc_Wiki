# SwapFlowItem — source reference

Assets.Behaviour.UI.SwapFlow/SwapFlowItem.cs · 113 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 16 | public class SwapFlowItem : MonoBehaviour, IPointerClickHandler, IEventSystemHandler, ITooltipTitleSource, ITooltipCustomSource |
| 31 | public InputAction Hotkey |
| 33 | public void SetWorkflow(int idx, FlowDiagram flow) |
| 59 | public void UpdateHighlight() |
| 64 | public void OnPointerClick(PointerEventData eventData) |
| 90 | public string GetTooltipTitle() |
| 100 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Workflow tabs, names, icons, and ordering](workflow-tabs-and-labels.md) |

## Sources

- `Assets.Behaviour.UI.SwapFlow/SwapFlowItem.cs:1`
