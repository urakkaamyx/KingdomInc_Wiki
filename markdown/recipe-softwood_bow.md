# Softwood Bow recipe

The materials used in this bow's construction aren't ideal, but it will do in a pinch.

## In the game

The materials used in this bow's construction aren't ideal, but it will do in a pinch.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 3.5 seconds |
| Research | [Softwood Bow](tech-softwood_bow.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Plank](item-wood_plank.md) | 2 |
| [Iron Ingot](item-iron_ingot.md) | 1 |
| [Rough String](item-rough_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Bow](item-softwood_bow.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 2),\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"rough_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"softwood_bow\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
