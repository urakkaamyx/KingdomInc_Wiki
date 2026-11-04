# Band of Tranquility recipe

The ring constantly sheds tiny seeds that drift off on the wind and sprout alien flowers in the countryside.

## In the game

The ring constantly sheds tiny seeds that drift off on the wind and sprout alien flowers in the countryside.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 9 seconds |
| Research | [Band of Tranquility](tech-ring_of_wisdom_2.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ring of Wisdom](item-ring_of_wisdom.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |
| [Precursor Symbiont](item-symbiote_reagent.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Band of Tranquility](item-ring_of_wisdom_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ring_of_wisdom\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1),\n\t\t\t\tnew CraftingReagent(\"symbiote_reagent\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ring_of_wisdom_2\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:180`
- `Assets.Source.Items/CraftingRecipe.cs:1`
