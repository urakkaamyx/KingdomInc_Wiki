# Ancient Wood Staff recipe

Tough and unyielding, but its delicate carved patterns suggest a hidden purpose beyond raw strength.

## In the game

Tough and unyielding, but its delicate carved patterns suggest a hidden purpose beyond raw strength.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 4 seconds |
| Research | [Ancient Wood Staff](tech-ancient_wood_staff.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 3 |
| [Arcanite Ingot](item-arcanium_ingot.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Staff](item-ancient_wood_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 3),\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ancient_wood_staff\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:112`
- `Assets.Source.Items/CraftingRecipe.cs:1`
