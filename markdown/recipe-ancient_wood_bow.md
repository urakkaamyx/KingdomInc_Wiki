# Ancient Wood Longbow recipe

The flexible-yet-sturdy limbs of this bow allow for both exceptional accuracy and astonishing rapid fire.

## In the game

The flexible-yet-sturdy limbs of this bow allow for both exceptional accuracy and astonishing rapid fire.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 3.5 seconds |
| Research | [Ancient Wood Longbow](tech-ancient_wood_bow.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 2 |
| [Arcanite Ingot](item-arcanium_ingot.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Longbow](item-ancient_wood_bow.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 2),\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ancient_wood_bow\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:154`
- `Assets.Source.Items/CraftingRecipe.cs:1`
