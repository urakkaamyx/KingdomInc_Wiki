# Embossed Mask recipe

Serves to obscure the wearer's identity and improve their lethality at the same time.

## In the game

Serves to obscure the wearer's identity and improve their lethality at the same time.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 3 seconds |
| Research | [Embossed Mask](tech-embossed_hat.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Embossed Leather](item-embossed_leather.md) | 2 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Embossed Mask](item-embossed_hat.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"embossed_leather\", 2),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"embossed_hat\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:81`
- `Assets.Source.Items/CraftingRecipe.cs:1`
