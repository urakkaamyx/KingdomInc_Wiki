# Engrave Weapon: Wisdom recipe

Engrave any weapon to provide additional Wisdom.

## In the game

Engrave any weapon to provide additional Wisdom.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3.5 seconds |
| Research | [Engrave Weapon: Wisdom](tech-engrave_weapon_wis.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Weapon (any type) | 1 |
| [Gold Wire](item-gold_wire.md) | 2 |
| [Silver Ingot](item-silver_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Engrave Weapon: Wisdom](enhancement-engrave_weapon_wis.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_96\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tcraftingReagent3,\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 2),\n\t\t\t\tnew CraftingReagent(\"silver_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_weapon_wis\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:186`
- `Assets.Source.Items/CraftingRecipe.cs:1`
