# Hulking Monstrosity recipe

A fearsome undead monster, composed of several corpses stitched together into a single brute.

## In the game

A fearsome undead monster, composed of several corpses stitched together into a single brute.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Necromancer](building-Necromancer.md) |
| Base crafting time | 28 seconds |
| Research | [Hulking Monstrosity](tech-hulking_monstrosity.md) |
| Currency consumed per batch | 2,480 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Buried Remains](item-buried_remains.md) | 3 |
| [Enchanted Thread](item-enchanted_cotton_thread.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Hulking Monstrosity](item-hulking_monstrosity.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_88\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"buried_remains\", 3),\n\t\t\t\tnew CraftingReagent(\"enchanted_cotton_thread\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 2480L)",
  "CraftingTimeMultiplier": "8f",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"hulking_monstrosity\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Necromancer.cs:73`
- `Assets.Source.Items/CraftingRecipe.cs:1`
