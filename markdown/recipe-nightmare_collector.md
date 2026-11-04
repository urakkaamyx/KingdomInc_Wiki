# Nightmare Collector recipe

The pinnacle of mago-tech engineering, designed to extract the living energy of a dreaming God.

## In the game

The pinnacle of mago-tech engineering, designed to extract the living energy of a dreaming God.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 17.5 seconds |
| Research | [Nightmare Collector](tech-nightmare_collector.md) |
| Currency consumed per batch | 257 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Nightmare Casing](item-nightmare_casing.md) | 1 |
| [Cleansed Nightmare](item-cleansed_nightmare.md) | 1 |
| [Decoded Writings](item-decoded_writings.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Nightmare Collector](item-nightmare_collector.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 257L)",
  "CraftingTimeMultiplier": "5f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"nightmare_casing\", 1),\n\t\t\t\tnew CraftingReagent(\"cleansed_nightmare\", 1),\n\t\t\t\tnew CraftingReagent(\"decoded_writings\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"nightmare_collector\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:251`
- `Assets.Source.Items/CraftingRecipe.cs:1`
