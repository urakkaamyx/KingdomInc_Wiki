# Simple Prayer recipe

A cleric offers a devout prayer to Saint Ilonia, generating a small amount of faith for your Kingdom.

## In the game

A cleric offers a devout prayer to Saint Ilonia, generating a small amount of faith for your Kingdom.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 6 seconds |
| Research | [Simple Prayer](tech-prayer_1.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Cleric | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| Custom selection | OutputCleric(0.1f) |
| Custom selection | OutputFaith(27f) |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons3_72\"",
  "BaseProductivity": "-999f",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[1] { craftingReagent }",
  "Results": "new CraftingResult[2]\n\t\t\t{\n\t\t\t\tOutputCleric(0.1f),\n\t\t\t\tOutputFaith(27f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:20`
- `Assets.Source.Items/CraftingRecipe.cs:1`
