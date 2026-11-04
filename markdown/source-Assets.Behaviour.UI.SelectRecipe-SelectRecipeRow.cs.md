# SelectRecipeRow — source reference

Assets.Behaviour.UI.SelectRecipe/SelectRecipeRow.cs · 93 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class SelectRecipeRow : MonoBehaviour, IPointerClickHandler, IEventSystemHandler, ITooltipTitleSource, ITooltipCustomSource |
| 31 | public CraftingRecipe Recipe { get; private set; } |
| 33 | public void SetRecipe(CraftingRecipe res, bool selected) |
| 67 | public void OnPointerClick(PointerEventData eventData) |
| 75 | public string GetTooltipTitle() |
| 80 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Build menu and recipe selection](buy-menu-and-recipe-selection.md) |

## Sources

- `Assets.Behaviour.UI.SelectRecipe/SelectRecipeRow.cs:1`
