# Butcher Cattle recipe

Turns a whole animal carcass into tasty meat and useful leather.

## In the game

Turns a whole animal carcass into tasty meat and useful leather.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Butcher](building-Butcher.md) |
| Base crafting time | 6 seconds |
| Research | [Butcher Cattle](tech-butcher_cattle.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Cattle](item-cattle.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Raw Beef](item-beef.md) | 2 |
| [Rough Leather](item-rough_leather.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_190\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"cattle\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[2]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"beef\", 2),\n\t\t\t\tnew CraftingResult(\"rough_leather\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Butcher.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
