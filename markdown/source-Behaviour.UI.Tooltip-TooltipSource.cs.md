# TooltipSource — source reference

Behaviour.UI.Tooltip/TooltipSource.cs · 104 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class TooltipSource : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler |
| 17 | public virtual UITooltip Prefab => UITooltipParent.TooltipPrefab |
| 19 | public string Title |
| 31 | public string BodyText |
| 43 | public virtual string GetTitle() |
| 52 | public virtual string GetBodyText() |
| 61 | public virtual void AddCustomContent(UITooltip tooltip) |
| 76 | public void OnPointerEnter(PointerEventData eventData) |
| 84 | public void OnPointerExit(PointerEventData eventData) |
| 94 | public void SetSource(GameObject source) |
| 99 | public void SetTooltip(string title, string body) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Behaviour.UI.Tooltip/TooltipSource.cs:1`
