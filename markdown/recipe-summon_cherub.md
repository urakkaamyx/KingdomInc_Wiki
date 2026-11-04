# Summon Cherub recipe

A small angelic creature empowered with healing magic.

## In the game

A small angelic creature empowered with healing magic.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Summoning Circle](building-SummoningCircle.md) |
| Base crafting time | 12 seconds |
| Research | [Summon Cherub](tech-summon_cherub.md) |
| Currency consumed per batch | 124 Faith |

## Ingredients

No item ingredients in the declared array. Currency costs and custom callbacks can still apply.

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Cherub](item-cherub.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Description": "\"@cherub_desc\"",
  "IconName": "\"Icons2_163\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[0]",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 124L)",
  "CraftingTimeMultiplier": "8f",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"cherub\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/SummoningCircle.cs:66`
- `Assets.Source.Items/CraftingRecipe.cs:1`
