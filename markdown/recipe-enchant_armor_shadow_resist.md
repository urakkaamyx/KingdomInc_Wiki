# Enchant Shield - Shadow Ward recipe

Enchants any Shield to reduce shadow damage taken in battle.

## In the game

Enchants any Shield to reduce shadow damage taken in battle.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Enchant Shield - Shadow Ward](tech-enchant_armor_shadow_resist.md) |
| Currency consumed per batch | 120 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Shield (any) | 1 |
| [Stalker Eye](item-stalker_eye.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchant Shield - Shadow Ward](enhancement-enchant_armor_shadow_resist.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_178\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tcraftingReagent2,\n\t\t\t\tnew CraftingReagent(\"stalker_eye\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 120L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_armor_shadow_resist\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:109`
- `Assets.Source.Items/CraftingRecipe.cs:1`
