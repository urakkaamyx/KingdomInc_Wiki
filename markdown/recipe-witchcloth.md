# Witchcloth recipe

A stupendous advancement in magical technology.

## In the game

A stupendous advancement in magical technology.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 2.5 seconds |
| Research | [Witchcloth](tech-witchcloth.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Embroidered Cotton](item-embroidered_cotton.md) | 1 |
| [Gizmo](item-gizmo.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Witchcloth](item-witchcloth.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"embroidered_cotton\", 1),\n\t\t\t\tnew CraftingReagent(\"gizmo\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"witchcloth\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:112`
- `Assets.Source.Items/CraftingRecipe.cs:1`
