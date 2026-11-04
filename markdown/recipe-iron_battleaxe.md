# Iron Battleaxe recipe

An enormous brute-force weapon made for enormous brute-force warriors.

## In the game

An enormous brute-force weapon made for enormous brute-force warriors.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 4.5 seconds |
| Research | [Iron Battleaxe](tech-iron_battleaxe.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 3 |
| [Softwood Plank](item-wood_plank.md) | 2 |
| [Rough String](item-rough_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Iron Battleaxe](item-iron_battleaxe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 3),\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 2),\n\t\t\t\tnew CraftingReagent(\"rough_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"iron_battleaxe\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:72`
- `Assets.Source.Items/CraftingRecipe.cs:1`
