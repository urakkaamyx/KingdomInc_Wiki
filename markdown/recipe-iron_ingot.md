# Iron Ingot recipe

Refined iron, forged into a shape that most other crafters know how to handle.

## In the game

Refined iron, forged into a shape that most other crafters know how to handle.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Forge](building-Forge.md) |
| Base crafting time | 2 seconds |
| Research | [Iron Ingot](tech-iron_ingot.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ore](item-iron_ore.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ore\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"iron_ingot\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Forge.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
