# Rough Leather Hat recipe

The itchy leather and coarse stitching will make any wearer go mad over time.

## In the game

The itchy leather and coarse stitching will make any wearer go mad over time.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 2.5 seconds |
| Research | [Rough Leather Hat](tech-rough_leather_hat.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Rough Leather](item-rough_leather.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Rough Leather Hat](item-rough_leather_hat.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"rough_leather\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"rough_leather_hat\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:32`
- `Assets.Source.Items/CraftingRecipe.cs:1`
