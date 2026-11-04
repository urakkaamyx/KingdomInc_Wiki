# Scroll of Disintegration recipe

This scroll's magic can be repeatedly evoked to deal heavy damage to powerful foes.

## In the game

This scroll's magic can be repeatedly evoked to deal heavy damage to powerful foes.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 3 seconds |
| Research | [Scroll of Disintegration](tech-scroll_of_damage.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Vellum](item-blank_vellum.md) | 1 |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |
| [Ember Briar](item-ember_briar.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Scroll of Disintegration](item-scroll_of_damage.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_vellum\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_ink\", 1),\n\t\t\t\tnew CraftingReagent(\"ember_briar\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"scroll_of_damage\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:89`
- `Assets.Source.Items/CraftingRecipe.cs:1`
