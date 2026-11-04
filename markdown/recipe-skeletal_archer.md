# Skeletal Archer recipe

A skeletal minion, its tendons reinforced to be able to draw back the bow made out of its own ribs.

## In the game

A skeletal minion, its tendons reinforced to be able to draw back the bow made out of its own ribs.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Necromancer](building-Necromancer.md) |
| Base crafting time | 20 seconds |
| Research | [Skeletal Archer](tech-skeletal_archer.md) |
| Currency consumed per batch | 520 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Buried Remains](item-buried_remains.md) | 1 |
| [Softwood Bow](item-softwood_bow.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Skeletal Archer](item-skeletal_archer.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_83\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"buried_remains\", 1),\n\t\t\t\tnew CraftingReagent(\"softwood_bow\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 520L)",
  "CraftingTimeMultiplier": "8f",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"skeletal_archer\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Necromancer.cs:25`
- `Assets.Source.Items/CraftingRecipe.cs:1`
