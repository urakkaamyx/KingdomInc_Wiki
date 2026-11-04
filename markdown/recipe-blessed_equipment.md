# Sanctified Equipment recipe

Extends a holy blessing over any non-weapon piece of equipment, increasing its Quality.

## In the game

Extends a holy blessing over any non-weapon piece of equipment, increasing its Quality.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 2 seconds |
| Research | [Sanctified Equipment](tech-blessed_equipment.md) |
| Currency consumed per batch | 145 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Equipment (non-weapon) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Sanctified Equipment](enhancement-blessed_equipment.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_76\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1] { craftingReagent3 }",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 145L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"blessed_equipment\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:88`
- `Assets.Source.Items/CraftingRecipe.cs:1`
