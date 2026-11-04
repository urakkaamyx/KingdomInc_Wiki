# Blank Vellum recipe

A traditional writing surface made from the skin of certain animals. Its inherent magical qualities make it very useful for writing prepared spells and arcane treatises.

## In the game

A traditional writing surface made from the skin of certain animals. Its inherent magical qualities make it very useful for writing prepared spells and arcane treatises.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 2.5 seconds |
| Research | [Blank Vellum](tech-blank_vellum.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Supple Leather](item-supple_leather.md) | 1 |
| [Crystalized Mana](item-crystal_mana.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Blank Vellum](item-blank_vellum.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"supple_leather\", 1),\n\t\t\t\tnew CraftingReagent(\"crystal_mana\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"blank_vellum\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:17`
- `Assets.Source.Items/CraftingRecipe.cs:1`
