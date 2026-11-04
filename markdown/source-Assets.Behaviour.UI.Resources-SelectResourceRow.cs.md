# SelectResourceRow — source reference

Assets.Behaviour.UI.Resources/SelectResourceRow.cs · 89 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class SelectResourceRow : MonoBehaviour, IPointerClickHandler, IEventSystemHandler, ITooltipTitleSource, ITooltipCustomSource |
| 32 | public ResourceItemType Resource { get; private set; } |
| 34 | public void SetResource(ResourceElement parent, ResourceItemType res, bool selected) |
| 66 | public void OnPointerClick(PointerEventData eventData) |
| 74 | public string GetTooltipTitle() |
| 79 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Resource quotas and supplier configuration](resource-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Resources/SelectResourceRow.cs:1`
