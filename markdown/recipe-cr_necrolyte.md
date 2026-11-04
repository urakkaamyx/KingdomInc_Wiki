# Introduction to Necromancy recipe

A few practical lessons in raising the dead allows a warlock to train as a Necromancer.

## In the game

A few practical lessons in raising the dead allows a warlock to train as a Necromancer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Necromancer](building-Necromancer.md) |
| Base crafting time | 12 seconds |
| Research | [Introduction to Necromancy](tech-cr_necrolyte.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Warlock](item-warlock.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |
| [Buried Remains](item-buried_remains.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Necrolyte](item-necrolyte.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_132\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"warlock\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1),\n\t\t\t\tnew CraftingReagent(\"buried_remains\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"necrolyte\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Necromancer.cs:89`
- `Assets.Source.Items/CraftingRecipe.cs:1`
