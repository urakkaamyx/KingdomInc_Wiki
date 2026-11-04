# Iron Armor recipe

Heavy and not very comfortable to wear, but provides sufficient protection at low cost.

## In the game

Heavy and not very comfortable to wear, but provides sufficient protection at low cost.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3 seconds |
| Research | [Iron Armor](tech-iron_armor.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 3 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Iron Armor](item-iron_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 3)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"iron_armor\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
