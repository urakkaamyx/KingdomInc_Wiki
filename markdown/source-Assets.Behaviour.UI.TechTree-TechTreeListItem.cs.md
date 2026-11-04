# TechTreeListItem — source reference

Assets.Behaviour.UI.TechTree/TechTreeListItem.cs · 132 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 15 | public class TechTreeListItem : MonoBehaviour, IPointerClickHandler, IEventSystemHandler, ITooltipTitleSource, ITooltipCustomSource |
| 43 | public void SetTech(TechNode node, bool purchased, bool locked) |
| 92 | public void OnPointerClick(PointerEventData eventData) |
| 115 | public string GetTooltipTitle() |
| 120 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Research tree and list interface](research-interface.md) |

## Sources

- `Assets.Behaviour.UI.TechTree/TechTreeListItem.cs:1`
