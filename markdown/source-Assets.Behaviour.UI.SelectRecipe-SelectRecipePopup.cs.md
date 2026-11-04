# SelectRecipePopup — source reference

Assets.Behaviour.UI.SelectRecipe/SelectRecipePopup.cs · 149 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 13 | public class SelectRecipePopup : UIPopupMenu |
| 32 | public bool ReopenBuyMenu { get; set; } |
| 34 | public WorldFlowRecipe Element { get; private set; } |
| 36 | public void SetRecipe(WorldFlowRecipe el) |
| 56 | public void UpdateRecipeList() |
| 78 | public void RecipeSelected(CraftingRecipe res) |
| 86 | public void ToggleSearch() |
| 106 | public void UpdateSearchText(bool force = false) |

## Documented by

| Wiki article |
| --- |
| [Build menu and recipe selection](buy-menu-and-recipe-selection.md) |

## Sources

- `Assets.Behaviour.UI.SelectRecipe/SelectRecipePopup.cs:1`
