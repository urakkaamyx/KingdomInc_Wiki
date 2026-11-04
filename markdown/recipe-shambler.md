# Undead Shambler recipe

A simple undead creature that even a rookie necromancer could reanimate.

## In the game

A simple undead creature that even a rookie necromancer could reanimate.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Necromancer](building-Necromancer.md) |
| Base crafting time | 16 seconds |
| Research | [Undead Shambler](tech-shambler.md) |
| Currency consumed per batch | 460 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Buried Remains](item-buried_remains.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Undead Shambler](item-shambler.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_86\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"buried_remains\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 460L)",
  "CraftingTimeMultiplier": "8f",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"shambler\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Necromancer.cs:10`
- `Assets.Source.Items/CraftingRecipe.cs:1`
