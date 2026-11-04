# Crafting, recipes, and automatic work

When ingredients are consumed, how long crafting takes, and what causes blocked crafts.

## Starting a craft

Each recipe declares reagent slots, counts, optional currency cost, result slots, and an unlock technology. The building must support the recipe's tag and the recipe technology must be purchased.

When no craft is running, a recipe building checks that every reagent input has its full required count. It then pays the recipe's currency cost and removes those items into a persistent CraftingInput. This starts a craft even without an automatic Worker; the Worker controls automatic progress, while manual clicks can progress a started craft.

## Timing

Unless explicitly set, recipe crafting time is (1.5 + 0.5 × total reagent item count) × CraftingTimeMultiplier seconds. Automatic progress per second is Speed divided by CraftingTime. Normal completion resets the running input, after which another ready craft can begin.

Every recipe output must have room before results are created. This includes an output for an unchanged or transformed input character as well as ordinary items. Recipes with probabilistic results use a single shared output and choose one result by the configured weights.

## Value

A recipe's default base value starts with the base values of value-affecting explicit reagents plus the gold equivalents of currency costs when CostIncreasesValue is enabled. The normal value multiplier is 1 + 0.15 × number of reagent slots + 0.15 if qualifying currency costs exist + 0.025 × CraftingTime; an explicit ValueMultiplier replaces it.

Filter-based reagents use preview items for the interface but default to not contributing preview value or input quality. Currency rewards are rolled at output quality, rounded, and credited when the craft completes.

## Sources

- `Assets.Source.Flow.Elements/RecipeElement.cs:96`
- `Assets.Source.Flow.Elements/RecipeElement.cs:185`
- `Assets.Source.Flow.Elements/RecipeElement.cs:280`
- `Assets.Source.Items/CraftingRecipe.cs:72`
- `Assets.Source.Items/CraftingRecipe.cs:217`
- `Assets.Source.Items/CraftingReagent.cs:30`
