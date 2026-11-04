# Simple Robe recipe

The robes provide no magical benefits, but an initiate wizard wouldn't want to be caught without one.

## In the game

The robes provide no magical benefits, but an initiate wizard wouldn't want to be caught without one.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 3.5 seconds |
| Research | [Simple Robe](tech-simple_robe.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Linen Cloth](item-linen_cloth.md) | 3 |
| [Linen Padding](item-linen_padding.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Simple Robe](item-simple_robe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"linen_cloth\", 3),\n\t\t\t\tnew CraftingReagent(\"linen_padding\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"simple_robe\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:20`
- `Assets.Source.Items/CraftingRecipe.cs:1`
