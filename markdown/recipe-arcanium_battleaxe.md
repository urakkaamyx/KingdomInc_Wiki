# Arcanite Cleaver recipe

For the mighty warrior that wants to fell trees and foes at the same time.

## In the game

For the mighty warrior that wants to fell trees and foes at the same time.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 4.5 seconds |
| Research | [Arcanite Cleaver](tech-arcanium_battleaxe.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Ingot](item-arcanium_ingot.md) | 3 |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 2 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Cleaver](item-arcanium_battleaxe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 3),\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 2),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"arcanium_battleaxe\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:217`
- `Assets.Source.Items/CraftingRecipe.cs:1`
