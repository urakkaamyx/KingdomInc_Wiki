# Ancient Woodcutter recipe

A sawblade imbued with magical fortitude, designed to cut even the most resilient logs.

## In the game

A sawblade imbued with magical fortitude, designed to cut even the most resilient logs.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3 seconds |
| Research | [Ancient Woodcutter](tech-ancient_woodcutter.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 2 |
| [Crystalized Mana](item-crystal_mana.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Woodcutter](item-ancient_woodcutter.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 2),\n\t\t\t\tnew CraftingReagent(\"crystal_mana\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ancient_woodcutter\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:140`
- `Assets.Source.Items/CraftingRecipe.cs:1`
