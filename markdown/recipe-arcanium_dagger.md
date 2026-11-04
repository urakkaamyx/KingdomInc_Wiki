# Arcanite Backstabber recipe

Its thin blade easily passes through even the sturdiest armor without snapping.

## In the game

Its thin blade easily passes through even the sturdiest armor without snapping.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3 seconds |
| Research | [Arcanite Backstabber](tech-arcanium_dagger.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Ingot](item-arcanium_ingot.md) | 2 |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Backstabber](item-arcanium_dagger.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 2),\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"arcanium_dagger\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:190`
- `Assets.Source.Items/CraftingRecipe.cs:1`
