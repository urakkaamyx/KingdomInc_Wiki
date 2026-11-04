# ArmoryItemRow — source reference

Assets.Behaviour.UI.ItemStore/ArmoryItemRow.cs · 98 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 12 | public class ArmoryItemRow : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler |
| 32 | public void SetItem(int channel, ItemType item, bool selected) |
| 69 | public void SetIcon(Sprite icon) |
| 74 | public string GetTooltipTitle() |
| 79 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 94 | public void OnPointerClick(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [Armory and Portal configuration](storage-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.ItemStore/ArmoryItemRow.cs:1`
