# Simple Burial recipe

A clean, no-frills way to lay your dead to rest.

## In the game

A clean, no-frills way to lay your dead to rest.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Graveyard](building-Graveyard.md) |
| Base crafting time | 7.5 seconds |
| Research | [Simple Burial](tech-simple_burial.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Human Remains](item-human_remains.md) | 1 |
| [Coffin](item-coffin.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| Custom selection | OutputRemains(0f) |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "BaseProductivity": "-999f",
  "IconName": "\"Icons2_82\"",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"human_remains\", 1),\n\t\t\t\tnew CraftingReagent(\"coffin\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1] { OutputRemains(0f) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Graveyard.cs:13`
- `Assets.Source.Items/CraftingRecipe.cs:1`
