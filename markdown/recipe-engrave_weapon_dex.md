# Engrave Weapon: Dexterity recipe

Engrave any weapon to provide additional Dexterity.

## In the game

Engrave any weapon to provide additional Dexterity.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3.5 seconds |
| Research | [Engrave Weapon: Dexterity](tech-engrave_weapon_dex.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Weapon (any type) | 1 |
| [Gold Wire](item-gold_wire.md) | 2 |
| [Resin](item-resin.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Engrave Weapon: Dexterity](enhancement-engrave_weapon_dex.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_94\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tcraftingReagent3,\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 2),\n\t\t\t\tnew CraftingReagent(\"resin\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_weapon_dex\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:156`
- `Assets.Source.Items/CraftingRecipe.cs:1`
