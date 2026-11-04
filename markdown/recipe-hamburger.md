# Hamburger recipe

An exotic delicacy based off an ancient recipe.

## In the game

An exotic delicacy based off an ancient recipe.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Kitchen](building-Kitchen.md) |
| Base crafting time | 6 seconds |
| Research | [Hamburger](tech-hamburger.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Raw Beef](item-beef.md) | 1 |
| [Wheat](item-wheat.md) | 1 |
| [Wild Lettuce](item-lettuce.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Hamburger](item-hamburger.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_193\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"beef\", 1),\n\t\t\t\tnew CraftingReagent(\"wheat\", 1),\n\t\t\t\tnew CraftingReagent(\"lettuce\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"hamburger\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Kitchen.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
