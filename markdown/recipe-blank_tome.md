# Blank Tome recipe

Pristine blank pages, ready to be filled with arcane incantations or prophetic writings.

## In the game

Pristine blank pages, ready to be filled with arcane incantations or prophetic writings.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 3.5 seconds |
| Research | [Blank Tome](tech-blank_tome.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Vellum](item-blank_vellum.md) | 3 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Blank Tome](item-blank_tome.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_vellum\", 3),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"blank_tome\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:30`
- `Assets.Source.Items/CraftingRecipe.cs:1`
