# Apothecary's Tome recipe

Contains a variety of medicinal recipes and practical tips for the aspiring doctor. Medical education not required.

## In the game

Contains a variety of medicinal recipes and practical tips for the aspiring doctor. Medical education not required.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 3 seconds |
| Research | [Apothecary's Tome](tech-tome_of_health.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Tome](item-blank_tome.md) | 1 |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |
| [Ember Briar](item-ember_briar.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Apothecary's Tome](item-tome_of_health.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_tome\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_ink\", 1),\n\t\t\t\tnew CraftingReagent(\"ember_briar\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tome_of_health\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:117`
- `Assets.Source.Items/CraftingRecipe.cs:1`
