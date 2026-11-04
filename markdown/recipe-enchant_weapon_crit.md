# Enchant Weapon - Critical Hit recipe

Enchants any weapon to add a chance to deal double damage.

A character can only benefit from a single source of Critical Hit.

## In the game

Enchants any weapon to add a chance to deal double damage.

A character can only benefit from a single source of Critical Hit.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Enchanter](building-Enchanter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Enchant Weapon - Critical Hit](tech-enchant_weapon_crit.md) |
| Currency consumed per batch | 230 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Weapon (any type) | 1 |
| [Stalker Eye](item-stalker_eye.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Enchant Weapon - Critical Hit](enhancement-enchant_weapon_crit.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_181\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tcraftingReagent,\n\t\t\t\tnew CraftingReagent(\"stalker_eye\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 230L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"enchant_weapon_crit\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Enchanter.cs:150`
- `Assets.Source.Items/CraftingRecipe.cs:1`
