# Iron Greatsword recipe

A huge blade that still feels surprisingly maneuverable in the right hands.

## In the game

A huge blade that still feels surprisingly maneuverable in the right hands.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 4.5 seconds |
| Research | [Iron Greatsword](tech-iron_greatsword.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 4 |
| [Softwood Plank](item-wood_plank.md) | 1 |
| [Rough String](item-rough_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Iron Greatsword](item-iron_greatsword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 4),\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 1),\n\t\t\t\tnew CraftingReagent(\"rough_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"iron_greatsword\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:58`
- `Assets.Source.Items/CraftingRecipe.cs:1`
