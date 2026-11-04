# Linen Cloth recipe

Coarse and crude, but provides protection from the elements.

## In the game

Coarse and crude, but provides protection from the elements.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 1 seconds |
| Research | [Linen Cloth](tech-linen_cloth.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Flax](item-flax.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Linen Cloth](item-linen_cloth.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "0.5f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"flax\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"linen_cloth\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:46`
- `Assets.Source.Items/CraftingRecipe.cs:1`
