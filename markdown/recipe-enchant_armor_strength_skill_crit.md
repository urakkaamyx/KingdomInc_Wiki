# Enchant Armor - Giant Strength recipe

Enchants any piece of Head or Chest armor to increase success chance on any Strength checks in combat. Also provides a small amount of Strength.

## In the game

Enchants any piece of Head or Chest armor to increase success chance on any Strength checks in combat. Also provides a small amount of Strength.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Enchant Armor - Giant Strength](tech-enchant_armor_strength_skill_crit.md) |
| Currency consumed per batch | 195 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Head or Chest armor | 1 |
| [Hamburger](item-hamburger.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchant Armor - Giant Strength](enhancement-enchant_armor_strength_skill_crit.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_184\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tcraftingReagent3,\n\t\t\t\tnew CraftingReagent(\"hamburger\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 195L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_armor_strength_skill_crit\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:135`
- `Assets.Source.Items/CraftingRecipe.cs:1`
