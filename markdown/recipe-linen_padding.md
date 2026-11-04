# Linen Padding recipe

Provides additional comfort when used in the production of heavier armor.

## In the game

Provides additional comfort when used in the production of heavier armor.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 2 seconds |
| Research | [Linen Padding](tech-linen_padding.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Linen Cloth](item-linen_cloth.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Linen Padding](item-linen_padding.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"linen_cloth\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"linen_padding\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
