# Nightmare Casing recipe

A hideously complex mago-tech invention, designed to constrain and direct the concentrated power of nightmare.

## In the game

A hideously complex mago-tech invention, designed to constrain and direct the concentrated power of nightmare.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 17.5 seconds |
| Research | [Nightmare Casing](tech-nightmare_casing.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 2 |
| [Purified Mago-tech](item-purified_tech.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Nightmare Casing](item-nightmare_casing.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "5f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 2),\n\t\t\t\tnew CraftingReagent(\"purified_tech\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"nightmare_casing\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:330`
- `Assets.Source.Items/CraftingRecipe.cs:1`
