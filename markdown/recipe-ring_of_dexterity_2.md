# Serpentine Band recipe

The living metal slithers around the wearer's finger as it sucks their blood for sustenance.

## In the game

The living metal slithers around the wearer's finger as it sucks their blood for sustenance.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 9 seconds |
| Research | [Serpentine Band](tech-ring_of_dexterity_2.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ring of Dexterity](item-ring_of_dexterity.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |
| [Precursor Symbiont](item-symbiote_reagent.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Serpentine Band](item-ring_of_dexterity_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ring_of_dexterity\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1),\n\t\t\t\tnew CraftingReagent(\"symbiote_reagent\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ring_of_dexterity_2\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:150`
- `Assets.Source.Items/CraftingRecipe.cs:1`
