# Embroider Clothing: Health recipe

Embroider a piece of light or medium armor to provide a minor Health bonus.

## In the game

Embroider a piece of light or medium armor to provide a minor Health bonus.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3 seconds |
| Research | [Embroider Clothing: Health](tech-engrave_light_armor_health.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Clothing (any type) | 1 |
| [Silver Thread](item-silver_thread.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Embroider Clothing: Health](enhancement-engrave_light_armor_health.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_93\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tcraftingReagent2,\n\t\t\t\tnew CraftingReagent(\"silver_thread\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_light_armor_health\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:67`
- `Assets.Source.Items/CraftingRecipe.cs:1`
