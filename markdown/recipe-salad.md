# Simple Salad recipe

Make sure to always eat your vegetables.

## In the game

Make sure to always eat your vegetables.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Campfire](building-Campfire.md) |
| Base crafting time | 5 seconds |
| Research | [Simple Salad](tech-salad.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Wild Lettuce](item-lettuce.md) | 1 |
| [Hardboiled Egg](item-cooked_egg.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Simple Salad](item-salad.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "ValueMultiplier": "2.0",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"lettuce\", 1),\n\t\t\t\tnew CraftingReagent(\"cooked_egg\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"salad\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Campfire.cs:36`
- `Assets.Source.Items/CraftingRecipe.cs:1`
