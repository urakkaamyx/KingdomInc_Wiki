# Crystalized Mana recipe

Pure magical energy distilled into a form that can be used by crafters other than enchanters.

## In the game

Pure magical energy distilled into a form that can be used by crafters other than enchanters.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 1.5 seconds |
| Research | [Crystalized Mana](tech-crystal_mana.md) |
| Currency consumed per batch | 30 Mana |

## Ingredients

No item ingredients in the declared array. Currency costs and custom callbacks can still apply.

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Crystalized Mana](item-crystal_mana.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[0]",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 30L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"crystal_mana\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:28`
- `Assets.Source.Items/CraftingRecipe.cs:1`
