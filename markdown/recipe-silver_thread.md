# Silver Thread recipe

Strong and flexible filaments of pure silver, perfect for detailed embroidering.

## In the game

Strong and flexible filaments of pure silver, perfect for detailed embroidering.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 2 seconds |
| Research | [Silver Thread](tech-silver_thread.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Silver Ingot](item-silver_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Silver Thread](item-silver_thread.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"silver_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"silver_thread\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:26`
- `Assets.Source.Items/CraftingRecipe.cs:1`
