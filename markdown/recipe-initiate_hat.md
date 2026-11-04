# Initiate's Hat recipe

Often given to young wizards during their training at the school of magic.

## In the game

Often given to young wizards during their training at the school of magic.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 3 seconds |
| Research | [Initiate's Hat](tech-initiate_hat.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Linen Cloth](item-linen_cloth.md) | 2 |
| [Linen Padding](item-linen_padding.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Initiate's Hat](item-initiate_hat.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"linen_cloth\", 2),\n\t\t\t\tnew CraftingReagent(\"linen_padding\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"initiate_hat\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:33`
- `Assets.Source.Items/CraftingRecipe.cs:1`
