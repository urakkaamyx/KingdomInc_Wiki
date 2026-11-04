# Commune with Nature recipe

Conversing with the spirits of the natural world allows a ritualist to train as a Shaman.

## In the game

Conversing with the spirits of the natural world allows a ritualist to train as a Shaman.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 10 seconds |
| Research | [Commune with Nature](tech-cr_shaman.md) |
| Currency consumed per batch | 190 Faith |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ritualist](item-ritualist.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Shaman](item-shaman.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_136\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ritualist\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 190L)",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"shaman\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:143`
- `Assets.Source.Items/CraftingRecipe.cs:1`
