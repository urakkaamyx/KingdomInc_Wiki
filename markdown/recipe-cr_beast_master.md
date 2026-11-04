# Feeding the Wildlife recipe

Getting in tune with nature allows a ranger to train as a Beast Master.

## In the game

Getting in tune with nature allows a ranger to train as a Beast Master.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Campfire](building-Campfire.md) |
| Base crafting time | 14 seconds |
| Research | [Feeding the Wildlife](tech-cr_beast_master.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ranger](item-ranger.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |
| [Seared Boar Steak](item-boar_steak.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Beast Master](item-beast_master.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_124\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ranger\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1),\n\t\t\t\tnew CraftingReagent(\"boar_steak\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"beast_master\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Campfire.cs:66`
- `Assets.Source.Items/CraftingRecipe.cs:1`
