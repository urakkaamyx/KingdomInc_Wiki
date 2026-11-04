# Enchant Armor - Protection recipe

Enchants any piece of Head or Chest armor to provide additional armor.

## In the game

Enchants any piece of Head or Chest armor to provide additional armor.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2 seconds |
| Research | [Enchant Armor - Protection](tech-enchant_armor_armor.md) |
| Currency consumed per batch | 292 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Head or Chest armor | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchant Armor - Protection](enhancement-enchant_armor_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_182\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1] { craftingReagent3 }",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 292L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_armor_armor\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:87`
- `Assets.Source.Items/CraftingRecipe.cs:1`
