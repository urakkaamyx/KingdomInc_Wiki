# Cotton Cloth recipe

A fine woven sheet of cotton fiber, ready to be processed into clothing.

## In the game

A fine woven sheet of cotton fiber, ready to be processed into clothing.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 1 seconds |
| Research | [Cotton Cloth](tech-cotton_cloth.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Cotton](item-cotton.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Cotton Cloth](item-cotton_cloth.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "0.5f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"cotton\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"cotton_cloth\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:59`
- `Assets.Source.Items/CraftingRecipe.cs:1`
