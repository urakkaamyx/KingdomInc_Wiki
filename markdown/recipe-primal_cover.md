# Primal Cover recipe

The shimmering surface of this armor serves to obscure the wearer's movements.

## In the game

The shimmering surface of this armor serves to obscure the wearer's movements.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 3.5 seconds |
| Research | [Primal Cover](tech-primal_cover.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Primal Leather](item-primal_leather.md) | 3 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Primal Cover](item-primal_cover.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"primal_leather\", 3),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"primal_cover\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:106`
- `Assets.Source.Items/CraftingRecipe.cs:1`
