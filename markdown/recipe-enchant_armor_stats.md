# Enchant Armor: Stats recipe

Enchants any piece of Head or Chest armor to provide boosts to all primary stats.

## In the game

Enchants any piece of Head or Chest armor to provide boosts to all primary stats.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2 seconds |
| Research | [Enchant Armor: Stats](tech-enchant_armor_stats.md) |
| Currency consumed per batch | 325 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Head or Chest armor | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchant Armor: Stats](enhancement-enchant_armor_stats.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_96\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1] { craftingReagent3 }",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 325L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_armor_stats\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:98`
- `Assets.Source.Items/CraftingRecipe.cs:1`
