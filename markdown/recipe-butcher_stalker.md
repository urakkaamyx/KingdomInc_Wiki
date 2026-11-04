# Butcher Stalker recipe

The animal's meat is stringy and inedible, but its other body parts are highly prized.

## In the game

The animal's meat is stringy and inedible, but its other body parts are highly prized.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Butcher](building-Butcher.md) |
| Base crafting time | 6 seconds |
| Research | [Butcher Stalker](tech-butcher_stalker.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Stalker](item-stalker.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Supple Leather](item-supple_leather.md) | 1 |
| [Stalker Eye](item-stalker_eye.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_176\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"stalker\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[2]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"supple_leather\", 1),\n\t\t\t\tnew CraftingResult(\"stalker_eye\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Butcher.cs:37`
- `Assets.Source.Items/CraftingRecipe.cs:1`
