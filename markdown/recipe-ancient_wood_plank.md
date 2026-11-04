# Ancient Wood Plank recipe

Sawn from a titanic tree, ready to be processed into a variety of resilient wooden components.

## In the game

Sawn from a titanic tree, ready to be processed into a variety of resilient wooden components.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Ancient Wood Plank](tech-ancient_wood_plank.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Log](item-ancient_wood_log.md) | 1 |
| [Ancient Woodcutter](item-ancient_woodcutter.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 3 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_wood_log\", 1),\n\t\t\t\tnew CraftingReagent(\"ancient_woodcutter\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ancient_wood_plank\", 3)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:99`
- `Assets.Source.Items/CraftingRecipe.cs:1`
