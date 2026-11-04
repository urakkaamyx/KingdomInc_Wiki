# Primal Mask recipe

Donning this mask for a prolonged period of time slowly drives the wearer mad with bloodlust.

## In the game

Donning this mask for a prolonged period of time slowly drives the wearer mad with bloodlust.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 3 seconds |
| Research | [Primal Mask](tech-primal_mask.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Primal Leather](item-primal_leather.md) | 2 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Primal Mask](item-primal_mask.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"primal_leather\", 2),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"primal_mask\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:119`
- `Assets.Source.Items/CraftingRecipe.cs:1`
