# Scholar's Hat recipe

The mark of a true intellectual, and a symbol of authority in wizarding cliques.

## In the game

The mark of a true intellectual, and a symbol of authority in wizarding cliques.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 3 seconds |
| Research | [Scholar's Hat](tech-cotton_hat.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Embroidered Cotton](item-embroidered_cotton.md) | 2 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Scholar's Hat](item-cotton_hat.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"embroidered_cotton\", 2),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"cotton_hat\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:85`
- `Assets.Source.Items/CraftingRecipe.cs:1`
