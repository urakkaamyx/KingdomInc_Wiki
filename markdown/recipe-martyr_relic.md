# Relic of the Martyr recipe

The bones of a fallen hero, carefully preserved in a gilded wooden locket. Bestows divine protection upon the bearer.

## In the game

The bones of a fallen hero, carefully preserved in a gilded wooden locket. Bestows divine protection upon the bearer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 3 seconds |
| Research | [Relic of the Martyr](tech-martyr_relic.md) |
| Currency consumed per batch | 305 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Human Remains](item-human_remains.md) | 1 |
| [Gold Ingot](item-gold_ingot.md) | 1 |
| [Petrified Wood](item-petrified_wood.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Relic of the Martyr](item-martyr_relic.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_78\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"human_remains\", 1),\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 305L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"martyr_relic\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:113`
- `Assets.Source.Items/CraftingRecipe.cs:1`
