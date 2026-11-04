# Enchant Weapon: Power recipe

Enchants an weapon to provide additional Combat Power.

## In the game

Enchants an weapon to provide additional Combat Power.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2 seconds |
| Research | [Enchant Weapon: Power](tech-enchant_weapon_power.md) |
| Currency consumed per batch | 515 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Weapon (any type) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchant Weapon: Power](enhancement-enchant_weapon_power.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_52\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1] { craftingReagent }",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 515L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_weapon_power\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:65`
- `Assets.Source.Items/CraftingRecipe.cs:1`
