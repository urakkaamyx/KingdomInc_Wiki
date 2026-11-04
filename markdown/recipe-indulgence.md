# Indulgence recipe

A document issued by the divine bureaucracy that promises to erase the bearer's sins upon death.

## In the game

A document issued by the divine bureaucracy that promises to erase the bearer's sins upon death.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 4 seconds |
| Research | [Indulgence](tech-indulgence.md) |
| Currency consumed per batch | 101 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Vellum](item-blank_vellum.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Indulgence](item-indulgence.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Faith, 101L)",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_vellum\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"indulgence\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:63`
- `Assets.Source.Items/CraftingRecipe.cs:1`
