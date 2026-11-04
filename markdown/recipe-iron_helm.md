# Iron Helm recipe

Wearing this for any length of time will make even the most stoic man pray for cloth padding.

## In the game

Wearing this for any length of time will make even the most stoic man pray for cloth padding.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 2.5 seconds |
| Research | [Iron Helm](tech-iron_helm.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Iron Helm](item-iron_helm.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"iron_helm\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:20`
- `Assets.Source.Items/CraftingRecipe.cs:1`
