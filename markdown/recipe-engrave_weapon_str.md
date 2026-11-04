# Engrave Weapon: Strength recipe

Engrave any weapon to provide additional Strength.

## In the game

Engrave any weapon to provide additional Strength.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3.5 seconds |
| Research | [Engrave Weapon: Strength](tech-engrave_weapon_str.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Weapon (any type) | 1 |
| [Gold Wire](item-gold_wire.md) | 2 |
| [Bone](item-bone.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Engrave Weapon: Strength](enhancement-engrave_weapon_str.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_91\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tcraftingReagent3,\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 2),\n\t\t\t\tnew CraftingReagent(\"bone\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_weapon_str\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:141`
- `Assets.Source.Items/CraftingRecipe.cs:1`
