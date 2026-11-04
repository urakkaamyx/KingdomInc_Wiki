# Embroider Clothing: Magic recipe

Embroider a piece of light or medium armor to provide additional Magic.

## In the game

Embroider a piece of light or medium armor to provide additional Magic.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3.5 seconds |
| Research | [Embroider Clothing: Magic](tech-engrave_light_armor_mag.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Clothing (any type) | 1 |
| [Silver Thread](item-silver_thread.md) | 2 |
| [Mushroom](item-mushroom.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Embroider Clothing: Magic](enhancement-engrave_light_armor_mag.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_99\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tcraftingReagent2,\n\t\t\t\tnew CraftingReagent(\"silver_thread\", 2),\n\t\t\t\tnew CraftingReagent(\"mushroom\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_light_armor_mag\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:111`
- `Assets.Source.Items/CraftingRecipe.cs:1`
