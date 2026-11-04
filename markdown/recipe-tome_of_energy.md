# Libram of Awakening recipe

A collection of honorable legends and inspiring anecdotes. Will encourage even the most melancholic serf.

## In the game

A collection of honorable legends and inspiring anecdotes. Will encourage even the most melancholic serf.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 3 seconds |
| Research | [Libram of Awakening](tech-tome_of_energy.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Tome](item-blank_tome.md) | 1 |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Libram of Awakening](item-tome_of_energy.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_ink\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tome_of_energy\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:145`
- `Assets.Source.Items/CraftingRecipe.cs:1`
