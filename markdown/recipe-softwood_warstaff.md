# Softwood Warstaff recipe

The wood is likely to fracture upon impact, making the iron reinforcements a necessity.

## In the game

The wood is likely to fracture upon impact, making the iron reinforcements a necessity.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 3.5 seconds |
| Research | [Softwood Warstaff](tech-softwood_warstaff.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Plank](item-wood_plank.md) | 2 |
| [Iron Ingot](item-iron_ingot.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Warstaff](item-softwood_warstaff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 2),\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"softwood_warstaff\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:35`
- `Assets.Source.Items/CraftingRecipe.cs:1`
