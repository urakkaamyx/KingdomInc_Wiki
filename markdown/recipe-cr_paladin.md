# Guardian's Pledge recipe

A sacred ritual to train a guardian into a Paladin.

## In the game

A sacred ritual to train a guardian into a Paladin.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 10 seconds |
| Research | [Guardian's Pledge](tech-cr_paladin.md) |
| Currency consumed per batch | 205 Faith |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Guardian](item-guardian.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Paladin](item-paladin.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_112\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"guardian\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 205L)",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"paladin\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:129`
- `Assets.Source.Items/CraftingRecipe.cs:1`
