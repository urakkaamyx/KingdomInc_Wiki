# SelectForestResourceRow — source reference

Assets.Behaviour.UI.Forest/SelectForestResourceRow.cs · 64 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class SelectForestResourceRow : MonoBehaviour, IPointerClickHandler, IEventSystemHandler, ITooltipTitleSource, ITooltipCustomSource |
| 30 | public ForestItemType Resource { get; private set; } |
| 32 | public void SetItem(Assets.Source.Flow.Elements.Forest parent, ForestItemType res, bool selected) |
| 41 | public void OnPointerClick(PointerEventData eventData) |
| 49 | public string GetTooltipTitle() |
| 54 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Forest crew and harvest controls](forest-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Forest/SelectForestResourceRow.cs:1`
