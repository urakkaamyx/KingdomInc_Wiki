# Elegant Ring recipe

A perfectly polished ring of alloyed gold and silver.

## In the game

A perfectly polished ring of alloyed gold and silver.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 2.5 seconds |
| Research | [Elegant Ring](tech-simple_ring.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 1 |
| [Silver Ingot](item-silver_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Elegant Ring](item-simple_ring.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"silver_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"simple_ring\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:38`
- `Assets.Source.Items/CraftingRecipe.cs:1`
