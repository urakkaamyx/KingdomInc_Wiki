# Arcanite Claymore recipe

The blade appears clumsy and cumbersome, but is surprisingly versatile in combat.

## In the game

The blade appears clumsy and cumbersome, but is surprisingly versatile in combat.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 4.5 seconds |
| Research | [Arcanite Claymore](tech-arcanium_greatsword.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Ingot](item-arcanium_ingot.md) | 4 |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Claymore](item-arcanium_greatsword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 4),\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"arcanium_greatsword\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:203`
- `Assets.Source.Items/CraftingRecipe.cs:1`
