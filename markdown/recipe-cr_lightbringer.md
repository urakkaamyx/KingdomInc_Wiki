# Prayer of Light recipe

Memorizing the entire thousand-page prayer allows a priest to train as a Lightbringer.

## In the game

Memorizing the entire thousand-page prayer allows a priest to train as a Lightbringer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 10 seconds |
| Research | [Prayer of Light](tech-cr_lightbringer.md) |
| Currency consumed per batch | 235 Faith |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Priest](item-priest.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Lightbringer](item-lightbringer.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_142\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"priest\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 235L)",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"lightbringer\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:171`
- `Assets.Source.Items/CraftingRecipe.cs:1`
