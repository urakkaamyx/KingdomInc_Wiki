# SwapFlowMenu — source reference

Assets.Behaviour.UI.SwapFlow/SwapFlowMenu.cs · 178 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class SwapFlowMenu : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler |
| 35 | public static SwapFlowMenu Instance { get; private set; } |
| 37 | public int MaxWidth |
| 57 | public void UpdateFlowButtons() |
| 86 | public void UpdateVisibleButtons() |
| 102 | public void CycleButtons(int cycle) |
| 109 | public void CycleCurrentFlow(int cycle) |
| 124 | public void UpdateHighlight() |
| 144 | public void OnPointerEnter(PointerEventData eventData) |
| 151 | public void OnPointerExit(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Workflow tabs, names, icons, and ordering](workflow-tabs-and-labels.md) |

## Sources

- `Assets.Behaviour.UI.SwapFlow/SwapFlowMenu.cs:1`
