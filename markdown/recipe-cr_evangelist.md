# Preaching to the Choir recipe

Powerful oration to the gathered followers allows a priest to train as an Evangelist.

## In the game

Powerful oration to the gathered followers allows a priest to train as an Evangelist.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 10 seconds |
| Research | [Preaching to the Choir](tech-cr_evangelist.md) |
| Currency consumed per batch | 225 Faith |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Priest](item-priest.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Evangelist](item-evangelist.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_140\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"priest\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 225L)",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"evangelist\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:157`
- `Assets.Source.Items/CraftingRecipe.cs:1`
