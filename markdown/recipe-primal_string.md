# Primal String recipe

A flexible ribbon cut from a single piece of treated animal hide.

## In the game

A flexible ribbon cut from a single piece of treated animal hide.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 2 seconds |
| Research | [Primal String](tech-primal_string.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Primal Leather](item-primal_leather.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Primal String](item-primal_string.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"primal_leather\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"primal_string\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:94`
- `Assets.Source.Items/CraftingRecipe.cs:1`
