# Engrave Weapon: Magic recipe

Engrave any weapon to provide additional Magic.

## In the game

Engrave any weapon to provide additional Magic.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3.5 seconds |
| Research | [Engrave Weapon: Magic](tech-engrave_weapon_mag.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Weapon (any type) | 1 |
| [Gold Wire](item-gold_wire.md) | 2 |
| [Mushroom](item-mushroom.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Engrave Weapon: Magic](enhancement-engrave_weapon_mag.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_95\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tcraftingReagent3,\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 2),\n\t\t\t\tnew CraftingReagent(\"mushroom\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_weapon_mag\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:171`
- `Assets.Source.Items/CraftingRecipe.cs:1`
