# Productivity and handcrafting

Bonus progress produces extra results without spending another set of ingredients.

## How bonus crafts work

Overseer grants 0.1 Productivity per installed upgrade. A recipe adds its BaseProductivity and clamps the final result to at least zero. During normal automatic progress, a separate productivity meter gains normal progress × Productivity; equipment recipes gain half that amount.

If productivity reaches 1, a completion uses one productivity point while keeping the current normal craft and its original ingredients. A subsequent normal completion consumes the running craft. This produces bonus batches without a fresh reagent set or another start payment.

Recipes with enhancement results explicitly disable productivity progress. Many character transformation, prayer, burial, or special chance recipes set BaseProductivity to −999, which suppresses ordinary building upgrade productivity after clamping. Manual Handcrafting Productivity prestige is added after that clamp, so it can still accrue bonus progress on such recipes unless enhancement output explicitly disables it.

## Manual crafting

A manual click on a running recipe adds Speed ÷ CraftingTime ÷ 2.5 to normal progress. Equivalently, each click supplies 0.4 seconds of work at the building's current speed. Clicking is available only while a craft exists and its normal progress is below 1.

Manual productivity uses the final building Productivity plus Handcrafting Productivity prestige, multiplied by the manual progress amount and halved for equipment. Because the prestige bonus is added after the recipe's negative BaseProductivity has already been clamped to zero, a −999 BaseProductivity recipe can still gain manual bonus progress. Enhancement recipes retain their explicit disable check. Manual resource clicks work differently: they purchase queued orders rather than directly adding recipe progress.

## Practical consequences

Faster workers and stacking produce normal and productivity progress faster, but cannot remove a resource quota bottleneck or full output. A bonus result still requires free output capacity.

The automatic recipe productivity meter only accrues while below 1, and completion creates at most one batch per building update. Frame timing and blocking can therefore affect throughput around very fast or high-productivity setups.

## Sources

- `Assets.Source.Flow.Upgrades/Overseer.cs:24`
- `Assets.Source.Flow.Elements/RecipeElement.cs:166`
- `Assets.Source.Flow.Elements/RecipeElement.cs:193`
- `Assets.Source.Flow.Elements/RecipeElement.cs:268`
- `Assets.Source.Flow.Elements/RecipeElement.cs:392`
- `Assets.Source.Flow.Elements/ResourceElement.cs:168`
