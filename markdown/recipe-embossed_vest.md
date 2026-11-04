# Embossed Vest recipe

The innate enchantments on this vest serve to increase the wearer's freedom of movement.

## In the game

The innate enchantments on this vest serve to increase the wearer's freedom of movement.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 3.5 seconds |
| Research | [Embossed Vest](tech-embossed_vest.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Embossed Leather](item-embossed_leather.md) | 3 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Embossed Vest](item-embossed_vest.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"embossed_leather\", 3),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"embossed_vest\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:68`
- `Assets.Source.Items/CraftingRecipe.cs:1`
