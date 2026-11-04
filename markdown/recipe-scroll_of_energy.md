# Scroll of Second Wind recipe

Even just holding it makes you feel revitalized. Reading the scroll will restore energy to the entire party.

## In the game

Even just holding it makes you feel revitalized. Reading the scroll will restore energy to the entire party.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 3 seconds |
| Research | [Scroll of Second Wind](tech-scroll_of_energy.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Vellum](item-blank_vellum.md) | 1 |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |
| [Stalker Eye](item-stalker_eye.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Scroll of Second Wind](item-scroll_of_energy.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_vellum\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_ink\", 1),\n\t\t\t\tnew CraftingReagent(\"stalker_eye\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"scroll_of_energy\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:103`
- `Assets.Source.Items/CraftingRecipe.cs:1`
