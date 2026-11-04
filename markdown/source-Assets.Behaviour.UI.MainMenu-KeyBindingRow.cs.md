# KeyBindingRow — source reference

Assets.Behaviour.UI.MainMenu/KeyBindingRow.cs · 92 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class KeyBindingRow : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, IPointerClickHandler |
| 31 | public void SetBinding(InputAction binding) |
| 45 | public void OnPointerClick(PointerEventData eventData) |
| 75 | public void OnPointerEnter(PointerEventData eventData) |
| 80 | public void OnPointerExit(PointerEventData eventData) |
| 85 | public void ClearListening() |

## Documented by

| Wiki article |
| --- |
| [Menus, save selection, music, and visual feedback](menus-saves-music-and-animation.md) |

## Sources

- `Assets.Behaviour.UI.MainMenu/KeyBindingRow.cs:1`
