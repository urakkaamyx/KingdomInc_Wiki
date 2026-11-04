# Imbue Dark Essence recipe

Weaves a powerful Dark Essence into any piece of equipment to significantly increase its quality.

## In the game

Weaves a powerful Dark Essence into any piece of equipment to significantly increase its quality.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 7.5 seconds |
| Research | [Imbue Dark Essence](tech-enchant_item_quality.md) |
| Currency consumed per batch | 698 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Equipment (any type) | 1 |
| [Dark Essence](item-dark_essence.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Imbue Dark Essence](enhancement-enchant_item_quality.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_221\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent((InventoryItem i) => i.Type is EquipmentItemType && i.CanEnhance(EnhancementType.Enchant), 1, \"ring_of_magic_2\", \"@enchant_reagent_equipment\"),\n\t\t\t\tnew CraftingReagent(\"dark_essence\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 698L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_item_quality\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:177`
- `Assets.Source.Items/CraftingRecipe.cs:1`
