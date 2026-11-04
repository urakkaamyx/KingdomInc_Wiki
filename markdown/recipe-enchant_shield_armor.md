# Enchant Shield - Protection recipe

Enchants any Shield to provide additional armor.

## In the game

Enchants any Shield to provide additional armor.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2 seconds |
| Research | [Enchant Shield - Protection](tech-enchant_shield_armor.md) |
| Currency consumed per batch | 189 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Shield (any) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchant Shield - Protection](enhancement-enchant_shield_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_97\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1] { craftingReagent2 }",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 189L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_shield_armor\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:124`
- `Assets.Source.Items/CraftingRecipe.cs:1`
