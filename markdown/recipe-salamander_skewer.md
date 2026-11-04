# Salamander Skewer recipe

A delicious fiery treat.

## In the game

A delicious fiery treat.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Kitchen](building-Kitchen.md) |
| Base crafting time | 5 seconds |
| Research | [Salamander Skewer](tech-salamander_skewer.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Salamander Haunch](item-salamander_haunch.md) | 1 |
| [Onion](item-onion.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Salamander Skewer](item-salamander_skewer.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_173\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"salamander_haunch\", 1),\n\t\t\t\tnew CraftingReagent(\"onion\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"salamander_skewer\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Kitchen.cs:24`
- `Assets.Source.Items/CraftingRecipe.cs:1`
