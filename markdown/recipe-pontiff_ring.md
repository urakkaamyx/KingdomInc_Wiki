# Pontiff's Ring recipe

A coveted signet ring that signifies the wearer's high standing in the Church of Saint Ilonia.

## In the game

A coveted signet ring that signifies the wearer's high standing in the Church of Saint Ilonia.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 2 seconds |
| Research | [Pontiff's Ring](tech-pontiff_ring.md) |
| Currency consumed per batch | 565 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Band of Tranquility](item-ring_of_wisdom_2.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Pontiff's Ring](item-pontiff_ring.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_77\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ring_of_wisdom_2\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 565L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"pontiff_ring\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:99`
- `Assets.Source.Items/CraftingRecipe.cs:1`
