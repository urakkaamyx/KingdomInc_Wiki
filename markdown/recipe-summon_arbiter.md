# Summon Arbiter recipe

The purest expression of divine punishment. None can escape his sword of wrath.

## In the game

The purest expression of divine punishment. None can escape his sword of wrath.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Summoning Circle](building-SummoningCircle.md) |
| Base crafting time | 16 seconds |
| Research | [Summon Arbiter](tech-summon_arbiter.md) |
| Currency consumed per batch | 475 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Claymore](item-arcanium_greatsword.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Arbiter](item-arbiter.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Description": "\"@arbiter_desc\"",
  "IconName": "\"Icons2_165\"",
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 475L)",
  "CraftingTimeMultiplier": "8f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"arcanium_greatsword\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"arbiter\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/SummoningCircle.cs:95`
- `Assets.Source.Items/CraftingRecipe.cs:1`
