# Cleansed Nightmare recipe

The toxic negative energy has been purified by the grace of Saint Ilonia. By Her grace, it can be put to a better use.

## In the game

The toxic negative energy has been purified by the grace of Saint Ilonia. By Her grace, it can be put to a better use.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 10 seconds |
| Research | [Cleansed Nightmare](tech-cleansed_nightmare.md) |
| Currency consumed per batch | 1,298 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Reconstructed Nightmare](item-reconstructed_nightmare.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Cleansed Nightmare](item-cleansed_nightmare.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "5f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"reconstructed_nightmare\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection(Currency.Faith, 1298L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"cleansed_nightmare\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:354`
- `Assets.Source.Items/CraftingRecipe.cs:1`
