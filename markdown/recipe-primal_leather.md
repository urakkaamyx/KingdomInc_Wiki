# Primal Leather recipe

An innovative tradition in magical technology.

## In the game

An innovative tradition in magical technology.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 2.5 seconds |
| Research | [Primal Leather](tech-primal_leather.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Embossed Leather](item-embossed_leather.md) | 1 |
| [Doodad](item-doodad.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Primal Leather](item-primal_leather.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"embossed_leather\", 1),\n\t\t\t\tnew CraftingReagent(\"doodad\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"primal_leather\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:125`
- `Assets.Source.Items/CraftingRecipe.cs:1`
