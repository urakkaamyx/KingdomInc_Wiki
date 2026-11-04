# Scroll of Radiance recipe

The scroll's magic is consumed upon use to restore a small amount of health to all party members.

## In the game

The scroll's magic is consumed upon use to restore a small amount of health to all party members.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 3 seconds |
| Research | [Scroll of Radiance](tech-scroll_of_aoe_healing.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Vellum](item-blank_vellum.md) | 1 |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |
| [Greater Healing Potion](item-greater_healing_potion.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Scroll of Radiance](item-scroll_of_aoe_healing.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_vellum\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_ink\", 1),\n\t\t\t\tnew CraftingReagent(\"greater_healing_potion\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"scroll_of_aoe_healing\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:75`
- `Assets.Source.Items/CraftingRecipe.cs:1`
