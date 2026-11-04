# Coffin recipe

A sturdy wooden box designed to hold the dead body of a human.

## In the game

A sturdy wooden box designed to hold the dead body of a human.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Coffin](tech-coffin.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Coffin](item-coffin.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"coffin\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:236`
- `Assets.Source.Items/CraftingRecipe.cs:1`
