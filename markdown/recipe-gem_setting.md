# Empty Setting recipe

A delicate gold structure that can be set with any cut gemstone.

## In the game

A delicate gold structure that can be set with any cut gemstone.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 2.5 seconds |
| Research | [Empty Setting](tech-gem_setting.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Gold Wire](item-gold_wire.md) | 1 |
| [Silver Ingot](item-silver_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Empty Setting](item-gem_setting.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 1),\n\t\t\t\tnew CraftingReagent(\"silver_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gem_setting\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:25`
- `Assets.Source.Items/CraftingRecipe.cs:1`
