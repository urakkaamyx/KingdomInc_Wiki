# Pyromancy and You: An Introduction recipe

A long-forgotten treatise on starting fires allows an elementalist to train as a Pyromancer.

## In the game

A long-forgotten treatise on starting fires allows an elementalist to train as a Pyromancer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 10 seconds |
| Research | [Pyromancy and You: An Introduction](tech-cr_pyromancer.md) |
| Currency consumed per batch | 192 Ingenuity |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Elementalist](item-elementalist.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Pyromancer](item-pyromancer.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_128\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"elementalist\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Ingenuity, 192L)",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"pyromancer\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:173`
- `Assets.Source.Items/CraftingRecipe.cs:1`
