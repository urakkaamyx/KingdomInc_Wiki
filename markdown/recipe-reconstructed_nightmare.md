# Reconstructed Nightmare recipe

A reconstituted essence of pure darkness.

## In the game

A reconstituted essence of pure darkness.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 10 seconds |
| Research | [Reconstructed Nightmare](tech-reconstructed_nightmare.md) |
| Currency consumed per batch | 13,283 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Fragmented Nightmare](item-fragmented_nightmare.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Reconstructed Nightmare](item-reconstructed_nightmare.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "5f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"fragmented_nightmare\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 13283L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"reconstructed_nightmare\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:221`
- `Assets.Source.Items/CraftingRecipe.cs:1`
