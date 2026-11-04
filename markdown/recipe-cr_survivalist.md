# Study on Phytotoxins recipe

Learning from the ancient masters of biology allows a ranger to train as a Survivalist.

## In the game

Learning from the ancient masters of biology allows a ranger to train as a Survivalist.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 10 seconds |
| Research | [Study on Phytotoxins](tech-cr_survivalist.md) |
| Currency consumed per batch | 182 Ingenuity |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ranger](item-ranger.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Survivalist](item-survivalist.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_126\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ranger\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Ingenuity, 182L)",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"survivalist\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:159`
- `Assets.Source.Items/CraftingRecipe.cs:1`
