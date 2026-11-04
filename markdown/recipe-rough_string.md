# Rough String recipe

Leather strips stretched into long fibers, ready to use in other crafting processes.

## In the game

Leather strips stretched into long fibers, ready to use in other crafting processes.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 2 seconds |
| Research | [Rough String](tech-rough_string.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Rough Leather](item-rough_leather.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Rough String](item-rough_string.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"rough_leather\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"rough_string\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
