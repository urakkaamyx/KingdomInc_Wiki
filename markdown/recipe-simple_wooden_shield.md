# Simple Wooden Shield recipe

Will stop a sword hit or two before splitering into kindling for the night's campfire.

## In the game

Will stop a sword hit or two before splitering into kindling for the night's campfire.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 3 seconds |
| Research | [Simple Wooden Shield](tech-simple_wooden_shield.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Plank](item-wood_plank.md) | 3 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Simple Wooden Shield](item-simple_wooden_shield.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 3)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"simple_wooden_shield\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:48`
- `Assets.Source.Items/CraftingRecipe.cs:1`
