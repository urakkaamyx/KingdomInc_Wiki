# ItemMenuRow — source reference

Assets.Behaviour.UI.ItemList/ItemMenuRow.cs · 208 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class ItemMenuRow : MonoBehaviour, IPointerEnterHandler, IEventSystemHandler, IPointerExitHandler, IPointerClickHandler |
| 55 | public ItemType Item { get; private set; } |
| 62 | public void SetItem(ItemType item, bool selected) |
| 81 | public void SetSelected(ItemType sel) |
| 190 | public void OnPointerClick(PointerEventData eventData) |
| 199 | public void OnPointerEnter(PointerEventData eventData) |
| 204 | public void OnPointerExit(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [The in-game item encyclopedia](item-encyclopedia.md) |

## Sources

- `Assets.Behaviour.UI.ItemList/ItemMenuRow.cs:1`
