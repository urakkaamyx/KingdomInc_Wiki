# Iron Dagger recipe

A simple iron dagger, for anyone wishing to train in the more subtle forms of combat.

## In the game

A simple iron dagger, for anyone wishing to train in the more subtle forms of combat.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3 seconds |
| Research | [Iron Dagger](tech-iron_dagger.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 2 |
| [Softwood Plank](item-wood_plank.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Iron Dagger](item-iron_dagger.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 2),\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"iron_dagger\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:45`
- `Assets.Source.Items/CraftingRecipe.cs:1`
