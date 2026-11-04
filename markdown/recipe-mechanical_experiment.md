# Mechanical Experimentation recipe

In search of new breakthroughs in mechanical science.

## In the game

In search of new breakthroughs in mechanical science.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 3 seconds |
| Research | [Mechanical Experimentation](tech-mechanical_experiment.md) |
| Currency reward per batch | 16 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Widget](item-widget.md) | 1 |
| [Iron Ingot](item-iron_ingot.md) | 2 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons3_69\"",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"widget\", 1),\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[0]",
  "CraftingReward": "new CurrencyCollection(Currency.Ingenuity, 16L)"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:63`
- `Assets.Source.Items/CraftingRecipe.cs:1`
