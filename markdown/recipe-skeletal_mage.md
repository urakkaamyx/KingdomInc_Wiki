# Skeletal Archmage recipe

A cunning undead sorcerer capable of raining hellfire upon your enemies.

## In the game

A cunning undead sorcerer capable of raining hellfire upon your enemies.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Necromancer](building-Necromancer.md) |
| Base crafting time | 20 seconds |
| Research | [Skeletal Archmage](tech-skeletal_mage.md) |
| Currency consumed per batch | 990 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Buried Remains](item-buried_remains.md) | 1 |
| [Ruby](item-gem_ruby.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Skeletal Archmage](item-skeletal_mage.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_85\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"buried_remains\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_ruby\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 990L)",
  "CraftingTimeMultiplier": "8f",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"skeletal_mage\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Necromancer.cs:57`
- `Assets.Source.Items/CraftingRecipe.cs:1`
