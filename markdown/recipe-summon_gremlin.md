# Summon Gremlin recipe

A tiny but ferocious demon that can be used to help train your adventurers and fight your wars.

## In the game

A tiny but ferocious demon that can be used to help train your adventurers and fight your wars.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Summoning Circle](building-SummoningCircle.md) |
| Base crafting time | 12 seconds |
| Research | [Summon Gremlin](tech-summon_gremlin.md) |
| Currency consumed per batch | 320 Mana |

## Ingredients

No item ingredients in the declared array. Currency costs and custom callbacks can still apply.

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Gremlin](item-gremlin.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_217\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[0]",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 320L)",
  "CraftingTimeMultiplier": "8f",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gremlin\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/SummoningCircle.cs:10`
- `Assets.Source.Items/CraftingRecipe.cs:1`
