# Rock Carving for Dummies recipe

A back-to-basics apprenticeship allows an elementalist to train as a Lithomancer.

## In the game

A back-to-basics apprenticeship allows an elementalist to train as a Lithomancer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 10 seconds |
| Research | [Rock Carving for Dummies](tech-cr_lithomancer.md) |
| Currency consumed per batch | 186 Ingenuity |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Elementalist](item-elementalist.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Lithomancer](item-lithomancer.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_130\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"elementalist\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Ingenuity, 186L)",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"lithomancer\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:187`
- `Assets.Source.Items/CraftingRecipe.cs:1`
