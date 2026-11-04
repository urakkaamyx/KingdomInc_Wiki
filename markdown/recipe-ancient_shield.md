# Bulwark of Ancients recipe

An impenetrable shield to protect the innocent and smite the villainous.

## In the game

An impenetrable shield to protect the innocent and smite the villainous.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 4 seconds |
| Research | [Bulwark of Ancients](tech-ancient_shield.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 3 |
| [Arcanite Ingot](item-arcanium_ingot.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Bulwark of Ancients](item-ancient_shield.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 3),\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ancient_shield\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:168`
- `Assets.Source.Items/CraftingRecipe.cs:1`
