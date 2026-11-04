# State Funeral recipe

A highly ornate funeral for only the most decorated of war heroes. Generates additional Faith based on the cleric's Wisdom.

## In the game

A highly ornate funeral for only the most decorated of war heroes. Generates additional Faith based on the cleric's Wisdom.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Graveyard](building-Graveyard.md) |
| Base crafting time | 30 seconds |
| Research | [State Funeral](tech-state_funeral.md) |
| Currency consumed per batch | 15 Crowns |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Human Remains](item-human_remains.md) | 1 |
| [Gilded Coffin](item-gilded_coffin.md) | 1 |
| Cleric | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| Custom selection | OutputRemains(0.2f) |
| Custom selection | Shrine.OutputCleric(0.3f) |
| Custom selection | Shrine.OutputFaith(290f) |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "BaseProductivity": "-999f",
  "CraftingTimeMultiplier": "10f",
  "IconName": "\"Icons2_90\"",
  "CraftingCost": "new CurrencyCollection(Currency.Crown, 15L)",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"human_remains\", 1),\n\t\t\t\tnew CraftingReagent(\"gilded_coffin\", 1),\n\t\t\t\tcraftingReagent\n\t\t\t}",
  "Results": "new CraftingResult[3]\n\t\t\t{\n\t\t\t\tOutputRemains(0.2f),\n\t\t\t\tShrine.OutputCleric(0.3f),\n\t\t\t\tShrine.OutputFaith(290f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Graveyard.cs:45`
- `Assets.Source.Items/CraftingRecipe.cs:1`
