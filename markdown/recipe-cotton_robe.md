# Scholar's Robe recipe

A robe worn by seasoned mages and clerics. The delicate symbols woven into the fabric enhance the wearer's magic.

## In the game

A robe worn by seasoned mages and clerics. The delicate symbols woven into the fabric enhance the wearer's magic.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 3.5 seconds |
| Research | [Scholar's Robe](tech-cotton_robe.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Embroidered Cotton](item-embroidered_cotton.md) | 3 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Scholar's Robe](item-cotton_robe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"embroidered_cotton\", 3),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"cotton_robe\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:72`
- `Assets.Source.Items/CraftingRecipe.cs:1`
