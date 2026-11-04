# Arcanite Ingot recipe

A wondrous metal that synthesizes both physical and magical components. Tough as nails and light as a feather.

## In the game

A wondrous metal that synthesizes both physical and magical components. Tough as nails and light as a feather.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Arcanite Ingot](tech-arcanium_ingot.md) |
| Currency consumed per batch | 20 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 1 |
| [Mercurial Flux](item-mercurial_flux.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Ingot](item-arcanium_ingot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"mercurial_flux\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 20L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"arcanium_ingot\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:14`
- `Assets.Source.Items/CraftingRecipe.cs:1`
