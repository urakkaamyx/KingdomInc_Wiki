# Enchanted Thread recipe

The magic woven into this thread prevent it from breaking even under severe strain.

## In the game

The magic woven into this thread prevent it from breaking even under severe strain.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2 seconds |
| Research | [Enchanted Thread](tech-enchanted_cotton_thread.md) |
| Currency consumed per batch | 15 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Cotton Cloth](item-cotton_cloth.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchanted Thread](item-enchanted_cotton_thread.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"cotton_cloth\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 15L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchanted_cotton_thread\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:38`
- `Assets.Source.Items/CraftingRecipe.cs:1`
