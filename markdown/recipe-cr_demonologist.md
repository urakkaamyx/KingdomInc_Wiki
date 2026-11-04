# Demonic Initiation recipe

A secret ritual known only to the hermit allows a warlock to train as a Demonologist.

## In the game

A secret ritual known only to the hermit allows a warlock to train as a Demonologist.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Summoning Circle](building-SummoningCircle.md) |
| Base crafting time | 12 seconds |
| Research | [Demonic Initiation](tech-cr_demonologist.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Warlock](item-warlock.md) | 1 |
| [Blank Tome](item-blank_tome.md) | 1 |
| [Gremlin](item-gremlin.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Demonologist](item-demonologist.md) | Transforms adventurer from input 0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_134\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"warlock\", 1),\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1),\n\t\t\t\tnew CraftingReagent(\"gremlin\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1] { CraftingResult.TransformAdventurer(0, \"demonologist\") }"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/SummoningCircle.cs:52`
- `Assets.Source.Items/CraftingRecipe.cs:1`
