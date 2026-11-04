# Arcanite Blade recipe

The magical properties of this sword cause its edge to always stay razor-sharp.

## In the game

The magical properties of this sword cause its edge to always stay razor-sharp.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3.5 seconds |
| Research | [Arcanite Blade](tech-arcanium_sword.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Ingot](item-arcanium_ingot.md) | 3 |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Blade](item-arcanium_sword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 3),\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"arcanium_sword\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:177`
- `Assets.Source.Items/CraftingRecipe.cs:1`
