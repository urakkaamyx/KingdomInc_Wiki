# Butcher Salamander recipe

A special technique to safely extract the boiling-hot meat of a Salamander.

## In the game

A special technique to safely extract the boiling-hot meat of a Salamander.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Butcher](building-Butcher.md) |
| Base crafting time | 6 seconds |
| Research | [Butcher Salamander](tech-butcher_salamander.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Salamander](item-salamander.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Salamander Haunch](item-salamander_haunch.md) | 3 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_172\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"salamander\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"salamander_haunch\", 3)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Butcher.cs:23`
- `Assets.Source.Items/CraftingRecipe.cs:1`
