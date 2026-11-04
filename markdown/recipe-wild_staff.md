# Staff of the Wild recipe

A simple staff that serves as a focus for nature-based divine magic.

## In the game

A simple staff that serves as a focus for nature-based divine magic.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 4 seconds |
| Research | [Staff of the Wild](tech-wild_staff.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Plank](item-wood_plank.md) | 3 |
| [Bone](item-bone.md) | 1 |
| [Silver Ingot](item-silver_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Staff of the Wild](item-wild_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 3),\n\t\t\t\tnew CraftingReagent(\"bone\", 1),\n\t\t\t\tnew CraftingReagent(\"silver_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"wild_staff\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:85`
- `Assets.Source.Items/CraftingRecipe.cs:1`
