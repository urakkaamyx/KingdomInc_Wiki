# Softwood Plank recipe

Freshly sawn from a softwood log, ready for further processing.

## In the game

Freshly sawn from a softwood log, ready for further processing.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 2 seconds |
| Research | [Softwood Plank](tech-wood_plank.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Log](item-wood_log.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Plank](item-wood_plank.md) | 3 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"wood_log\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"wood_plank\", 3)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:73`
- `Assets.Source.Items/CraftingRecipe.cs:1`
