# Transmute Metals recipe

Employs a secret alchemical catalyst to transmute common iron into precious metals.

## In the game

Employs a secret alchemical catalyst to transmute common iron into precious metals.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 3 seconds |
| Research | [Transmute Metals](tech-transmute_metals.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 2 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 2 |
| [Silver Ingot](item-silver_ingot.md) | 2 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons2_197\"",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 2),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[2]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gold_ingot\", 2),\n\t\t\t\tnew CraftingResult(\"silver_ingot\", 2)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:23`
- `Assets.Source.Items/CraftingRecipe.cs:1`
