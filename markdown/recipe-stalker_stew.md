# Stalker Stew recipe

Deliciously oniony. Just don't ask about the other ingredient.

## In the game

Deliciously oniony. Just don't ask about the other ingredient.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Kitchen](building-Kitchen.md) |
| Base crafting time | 6 seconds |
| Research | [Stalker Stew](tech-stalker_stew.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Stalker Eye](item-stalker_eye.md) | 1 |
| [Onion](item-onion.md) | 1 |
| [Wild Onion](item-wild_onion.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Stalker Stew](item-stalker_stew.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_179\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"stalker_eye\", 1),\n\t\t\t\tnew CraftingReagent(\"onion\", 1),\n\t\t\t\tnew CraftingReagent(\"wild_onion\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"stalker_stew\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Kitchen.cs:39`
- `Assets.Source.Items/CraftingRecipe.cs:1`
