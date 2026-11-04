# Parade Armor recipe

A suit of armor made not for protection, but for showing off your wealth and status.

## In the game

A suit of armor made not for protection, but for showing off your wealth and status.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3 seconds |
| Research | [Parade Armor](tech-gold_armor.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 1 |
| [Gold Ingot](item-gold_ingot.md) | 1 |
| [Silver Ingot](item-silver_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Parade Armor](item-gold_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"silver_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gold_armor\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:86`
- `Assets.Source.Items/CraftingRecipe.cs:1`
