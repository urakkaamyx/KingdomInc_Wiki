# ItemMenuRecipe — source reference

Assets.Behaviour.UI.ItemList/ItemMenuRecipe.cs · 233 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 18 | public class ItemMenuRecipe : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource, IPointerClickHandler, IEventSystemHandler, IBeginDragHandler, IDragHandler |
| 39 | public void SetRecipe(CraftingRecipe cr) |
| 56 | public void SetArena() |
| 73 | public void SetTrainingGrounds() |
| 90 | public void SetResource(ResourceItemType rit) |
| 118 | public void SetForest(ForestItemType rit) |
| 130 | public void SetQuest(Quest source) |
| 148 | public void SetDungeon(DungeonType source) |
| 166 | public void SetLocked(TechNode req) |
| 189 | public string GetTooltipTitle() |
| 194 | public void AddTooltipCustomContent(UITooltip tooltip) |
| 199 | public void OnPointerClick(PointerEventData eventData) |
| 207 | public void OnBeginDrag(PointerEventData eventData) |
| 230 | public void OnDrag(PointerEventData eventData) |

## Documented by

| Wiki article |
| --- |
| [The in-game item encyclopedia](item-encyclopedia.md) |

## Sources

- `Assets.Behaviour.UI.ItemList/ItemMenuRecipe.cs:1`
