# Enchant Food: Deliciousness recipe

Enchants any food with a powerful spell that improves its taste. Quality is increased as a side effect.

## In the game

Enchants any food with a powerful spell that improves its taste. Quality is increased as a side effect.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2 seconds |
| Research | [Enchant Food: Deliciousness](tech-enchant_food_quality.md) |
| Currency consumed per batch | 132 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Food (any type) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchant Food: Deliciousness](enhancement-enchant_food_quality.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_206\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent((InventoryItem i) => i.Type is EquipmentItemType { Slot: EquipmentSlot.Food } && i.CanEnhance(EnhancementType.Enchant), 1, \"hamburger\", \"@enchant_reagent_food\")\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 132L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_food_quality\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:51`
- `Assets.Source.Items/CraftingRecipe.cs:1`
