# UIBlocksZoom — source reference

Assets.Behaviour.UI.Shared/UIBlocksZoom.cs · 27 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class UIBlocksZoom : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler |
| 11 | public static bool Blocked => blockingZoom.Count > 0 |
| 18 | public void OnPointerEnter(PointerEventData eventData) |
| 23 | public void OnPointerExit(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Tooltips, warnings, notifications, and tutorial cues](tooltips-warnings-and-tutorial.md) |

## Sources

- `Assets.Behaviour.UI.Shared/UIBlocksZoom.cs:1`
