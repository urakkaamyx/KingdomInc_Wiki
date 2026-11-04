# Enchanted Ink recipe

Jet-black ink imbued with powerful magical energy, suitable for writing spell scrolls and arcane tomes.

## In the game

Jet-black ink imbued with powerful magical energy, suitable for writing spell scrolls and arcane tomes.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Enchanted Ink](tech-enchanted_ink.md) |
| Currency consumed per batch | 85 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Stalker Eye](item-stalker_eye.md) | 1 |
| [Glass Vial](item-glass_vial.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"stalker_eye\", 1),\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 85L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchanted_ink\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:207`
- `Assets.Source.Items/CraftingRecipe.cs:1`
