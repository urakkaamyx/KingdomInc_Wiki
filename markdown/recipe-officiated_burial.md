# Officiated Burial recipe

Send a Cleric to lead the mourners in solemn prayer. Generates additional Faith based on the cleric's Wisdom.

## In the game

Send a Cleric to lead the mourners in solemn prayer. Generates additional Faith based on the cleric's Wisdom.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Graveyard](building-Graveyard.md) |
| Base crafting time | 18 seconds |
| Research | [Officiated Burial](tech-officiated_burial.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Human Remains](item-human_remains.md) | 1 |
| [Coffin](item-coffin.md) | 1 |
| Cleric | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| Custom selection | OutputRemains(0f) |
| Custom selection | Shrine.OutputCleric(0.15f) |
| Custom selection | Shrine.OutputFaith(100f) |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "BaseProductivity": "-999f",
  "IconName": "\"Icons2_89\"",
  "CraftingTimeMultiplier": "6f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"human_remains\", 1),\n\t\t\t\tnew CraftingReagent(\"coffin\", 1),\n\t\t\t\tcraftingReagent\n\t\t\t}",
  "Results": "new CraftingResult[3]\n\t\t\t{\n\t\t\t\tOutputRemains(0f),\n\t\t\t\tShrine.OutputCleric(0.15f),\n\t\t\t\tShrine.OutputFaith(100f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Graveyard.cs:26`
- `Assets.Source.Items/CraftingRecipe.cs:1`
