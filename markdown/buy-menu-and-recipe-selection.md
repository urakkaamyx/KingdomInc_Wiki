# Build menu and recipe selection

Categories, search, selected recipes, ingredient previews, and changing machine configuration.

## Build categories and search

The build menu lists buildable machine types under category tabs. Empty categories are gray and cannot be selected. Search hides the tabs and matches all typed words, case-insensitively, against translated label or description. Blank search produces no result list in this implementation.

## Recipe selection

The current recipe is shown first above a spacer, followed by the other recipes available to that machine. Search matches every nonempty word against recipe name or description. Changing machine type resets the search state. Each recipe row shows reagent icons/counts and direct currency crafting costs; hovering shows equipment slot, description and detailed recipe results.

## Changing a recipe

Selection clears and rebuilds the machine’s IO and refreshes its label/icon. The adapter attempts to reconnect old pipes by matching port indices that still exist. Input-side reconnections retain their old waypoints; output-side reconstruction does not explicitly copy them. Do not assume changing recipes preserves the meaning of each indexed ingredient connection.

## Tutorial behavior

Recipe selection is blocked during the initial blackout. New machine and recipe adapters often open a configuration popup one frame after placement. Several ReopenBuyMenu properties are recorded but their selection callbacks only discard the value, so they are not a reliable promise that every configuration returns to the build menu.

## Sources

- `Assets.Behaviour.UI.BuyMenu/BuyMenuTab.cs:27`
- `Assets.Behaviour.UI.BuyMenu/ElementBuyMenu.cs:38`
- `Assets.Behaviour.UI.SelectRecipe/SelectRecipePopup.cs:36`
- `Assets.Behaviour.UI.SelectRecipe/SelectRecipeRow.cs:33`
- `Assets.Behaviour.Flow.Elements/WorldFlowRecipe.cs:21`
