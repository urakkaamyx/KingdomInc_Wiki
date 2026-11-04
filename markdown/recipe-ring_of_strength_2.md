# Band of the Cyclops recipe

The unblinking eye that adorns this ring stares back at the wearer incessantly.

## In the game

The unblinking eye that adorns this ring stares back at the wearer incessantly.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 9 seconds |
| Research | [Band of the Cyclops](tech-ring_of_strength_2.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ring of Strength](item-ring_of_strength.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |
| [Precursor Symbiont](item-symbiote_reagent.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Band of the Cyclops](item-ring_of_strength_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ring_of_strength\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1),\n\t\t\t\tnew CraftingReagent(\"symbiote_reagent\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ring_of_strength_2\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:135`
- `Assets.Source.Items/CraftingRecipe.cs:1`
