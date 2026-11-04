# Anatomy Lesson recipe

Learning from the masters of precision allows a thief to train as an Assassin.

## In the game

Learning from the masters of precision allows a thief to train as an Assassin.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Butcher](building-Butcher.md) |
| Base crafting time | 12 seconds |
| Research | [Anatomy Lesson](tech-cr_assassin.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Thief](item-thief.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |
| [Stalker](item-stalker.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Assassin](item-assassin.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_120\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"thief\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1),\n\t\t\t\tnew CraftingReagent(\"stalker\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"assassin\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Butcher.cs:52`
- `Assets.Source.Items/CraftingRecipe.cs:1`
