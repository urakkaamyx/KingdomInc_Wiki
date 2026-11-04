# NightmareDisplay — source reference

Assets.Behaviour.UI.Prestige/NightmareDisplay.cs · 72 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class NightmareDisplay : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler |
| 21 | public static NightmareDisplay Instance { get; private set; } |
| 33 | public void UpdateNightmare() |
| 46 | public void DoAwaken() |
| 53 | public void OpenDetails() |
| 63 | public void OnPointerEnter(PointerEventData eventData) |
| 68 | public void OnPointerExit(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Ascension and what carries over](ascension.md) |

## Sources

- `Assets.Behaviour.UI.Prestige/NightmareDisplay.cs:1`
