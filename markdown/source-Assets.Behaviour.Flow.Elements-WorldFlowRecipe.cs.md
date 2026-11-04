# WorldFlowRecipe — source reference

Assets.Behaviour.Flow.Elements/WorldFlowRecipe.cs · 118 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 15 | public class WorldFlowRecipe : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 19 | public RecipeElement Element { get; private set; } |
| 28 | public void UpdateRecipe() |
| 34 | public void SetRecipe(CraftingRecipe res) |
| 72 | public void ShowRecipePopup() |
| 82 | public void DelayShowRecipePopup() |
| 94 | public string GetTooltipTitle() |
| 103 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Build menu and recipe selection](buy-menu-and-recipe-selection.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowRecipe.cs:1`
