# Hardboiled Egg recipe

Not the tastiest meal, but it'll fill your stomach in a pinch.

## In the game

Not the tastiest meal, but it'll fill your stomach in a pinch.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Campfire](building-Campfire.md) |
| Base crafting time | 8 seconds |
| Research | [Hardboiled Egg](tech-cooked_egg.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Small Bird Egg](item-bird_egg.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Hardboiled Egg](item-cooked_egg.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "ValueMultiplier": "2.0",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"bird_egg\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"cooked_egg\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Campfire.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
