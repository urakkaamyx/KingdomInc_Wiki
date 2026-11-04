# Iron Sword recipe

A simple iron sword, suitable for any initiate knight or rookie adventurer.

## In the game

A simple iron sword, suitable for any initiate knight or rookie adventurer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3.5 seconds |
| Research | [Iron Sword](tech-iron_sword.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 3 |
| [Softwood Plank](item-wood_plank.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Iron Sword](item-iron_sword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 3),\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"iron_sword\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:32`
- `Assets.Source.Items/CraftingRecipe.cs:1`
