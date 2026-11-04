# Gold Ingot recipe

A small bar of purified gold, ready to be turned into art.

## In the game

A small bar of purified gold, ready to be turned into art.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Forge](building-Forge.md) |
| Base crafting time | 2 seconds |
| Research | [Gold Ingot](tech-gold_ingot.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Gold Ore](item-gold_ore.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gold_ore\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gold_ingot\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Forge.cs:20`
- `Assets.Source.Items/CraftingRecipe.cs:1`
