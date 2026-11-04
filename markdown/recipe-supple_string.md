# Supple String recipe

A flexible, braided leather cord that somehow seems almost unbreakable.

## In the game

A flexible, braided leather cord that somehow seems almost unbreakable.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 2 seconds |
| Research | [Supple String](tech-supple_string.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Supple Leather](item-supple_leather.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Supple String](item-supple_string.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"supple_leather\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"supple_string\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:56`
- `Assets.Source.Items/CraftingRecipe.cs:1`
