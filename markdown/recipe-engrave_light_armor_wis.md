# Embroider Clothing: Wisdom recipe

Embroider a piece of light or medium armor to provide additional Wisdom.

## In the game

Embroider a piece of light or medium armor to provide additional Wisdom.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3.5 seconds |
| Research | [Embroider Clothing: Wisdom](tech-engrave_light_armor_wis.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Clothing (any type) | 1 |
| [Silver Thread](item-silver_thread.md) | 2 |
| [Gold Ingot](item-gold_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Embroider Clothing: Wisdom](enhancement-engrave_light_armor_wis.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_100\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tcraftingReagent2,\n\t\t\t\tnew CraftingReagent(\"silver_thread\", 2),\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_light_armor_wis\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:126`
- `Assets.Source.Items/CraftingRecipe.cs:1`
