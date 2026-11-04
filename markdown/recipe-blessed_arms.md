# Blessed Armaments recipe

Extends a holy blessing over any weapon, increasing its Quality.

## In the game

Extends a holy blessing over any weapon, increasing its Quality.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 2 seconds |
| Research | [Blessed Armaments](tech-blessed_arms.md) |
| Currency consumed per batch | 195 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Weapon (any type) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Blessed Armaments](enhancement-blessed_arms.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_75\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1] { craftingReagent2 }",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 195L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"blessed_arms\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:77`
- `Assets.Source.Items/CraftingRecipe.cs:1`
