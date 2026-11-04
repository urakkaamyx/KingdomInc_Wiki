# Seared Boar Steak recipe

The simplest way to grill a piece of meat: Just throw it in a fire.

## In the game

The simplest way to grill a piece of meat: Just throw it in a fire.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Campfire](building-Campfire.md) |
| Base crafting time | 8 seconds |
| Research | [Seared Boar Steak](tech-boar_steak.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Boar Meat](item-boar_meat.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Seared Boar Steak](item-boar_steak.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "4f",
  "ValueMultiplier": "2.0",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"boar_meat\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"boar_steak\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Campfire.cs:22`
- `Assets.Source.Items/CraftingRecipe.cs:1`
