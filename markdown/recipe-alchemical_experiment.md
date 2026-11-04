# Alchemical Experimentation recipe

In search of new breakthroughs in alchemical knowledge.

## In the game

In search of new breakthroughs in alchemical knowledge.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 2.5 seconds |
| Research | [Alchemical Experimentation](tech-alchemical_experiment.md) |
| Currency reward per batch | 14 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Gizmo](item-gizmo.md) | 1 |
| [Soothing Herbs](item-soothing_herbs.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons3_67\"",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gizmo\", 1),\n\t\t\t\tnew CraftingReagent(\"soothing_herbs\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[0]",
  "CraftingReward": "new CurrencyCollection(Currency.Ingenuity, 14L)"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:75`
- `Assets.Source.Items/CraftingRecipe.cs:1`
