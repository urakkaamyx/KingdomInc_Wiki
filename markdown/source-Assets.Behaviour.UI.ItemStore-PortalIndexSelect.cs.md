# PortalIndexSelect — source reference

Assets.Behaviour.UI.ItemStore/PortalIndexSelect.cs · 63 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class PortalIndexSelect : MonoBehaviour, IPointerClickHandler, IEventSystemHandler, ITooltipTitleSource, ITooltipCustomSource |
| 29 | public void SetIndex(int channel, bool selected) |
| 36 | public void SetContent(InventoryItem content) |
| 44 | public void OnPointerClick(PointerEventData eventData) |
| 49 | public void SetSelected(int ch) |
| 54 | public string GetTooltipTitle() |
| 59 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Armory and Portal configuration](storage-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.ItemStore/PortalIndexSelect.cs:1`
