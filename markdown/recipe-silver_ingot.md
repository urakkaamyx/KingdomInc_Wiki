# Silver Ingot recipe

A small bar of purified silver, ready to be turned into art.

## In the game

A small bar of purified silver, ready to be turned into art.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Forge](building-Forge.md) |
| Base crafting time | 2 seconds |
| Research | [Silver Ingot](tech-silver_ingot.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Silver Ore](item-silver_ore.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Silver Ingot](item-silver_ingot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"silver_ore\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"silver_ingot\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Forge.cs:32`
- `Assets.Source.Items/CraftingRecipe.cs:1`
