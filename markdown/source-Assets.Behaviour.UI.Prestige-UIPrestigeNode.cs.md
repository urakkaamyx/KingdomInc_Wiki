# UIPrestigeNode — source reference

Assets.Behaviour.UI.Prestige/UIPrestigeNode.cs · 127 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class UIPrestigeNode : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, IPointerClickHandler |
| 34 | public void SetPrestigeNode(PrestigeNode node) |
| 60 | public void UpdateNode() |
| 67 | public string GetTooltipTitle() |
| 72 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 101 | public void OnPointerEnter(PointerEventData eventData) |
| 106 | public void OnPointerExit(PointerEventData eventData) |
| 111 | public void OnPointerClick(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Prestige perks and refunds](prestige-perks.md) |

## Sources

- `Assets.Behaviour.UI.Prestige/UIPrestigeNode.cs:1`
