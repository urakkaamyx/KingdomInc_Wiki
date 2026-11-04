# Sinister Prodigy recipe

Breeds more Symbionts by exposing them to the corrupting essence of darkness.

## In the game

Breeds more Symbionts by exposing them to the corrupting essence of darkness.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Sinister Prodigy](tech-symbiote_breeding.md) |
| Currency consumed per batch | 313 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Precursor Symbiont](item-symbiote_reagent.md) | 1 |
| [Dark Essence](item-dark_essence.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Precursor Symbiont](item-symbiote_reagent.md) | 2 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"symbiote_reagent\", 1),\n\t\t\t\tnew CraftingReagent(\"dark_essence\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 313L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"symbiote_reagent\", 2)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:193`
- `Assets.Source.Items/CraftingRecipe.cs:1`
