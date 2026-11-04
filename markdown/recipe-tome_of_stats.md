# Manual of Self-Improvement recipe

Describes a hundred daily habits to improve the reader's life in almost every way possible.

## In the game

Describes a hundred daily habits to improve the reader's life in almost every way possible.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 3 seconds |
| Research | [Manual of Self-Improvement](tech-tome_of_stats.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Tome](item-blank_tome.md) | 1 |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |
| [Elixir of Mastery](item-stats_potion.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Manual of Self-Improvement](item-tome_of_stats.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_ink\", 1),\n\t\t\t\tnew CraftingReagent(\"stats_potion\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tome_of_stats\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:131`
- `Assets.Source.Items/CraftingRecipe.cs:1`
