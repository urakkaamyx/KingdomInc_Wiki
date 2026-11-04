# Elixir of Alacrity recipe

A highly concentrated emerald liquid. It hones the drinker's quick wit and reflexes, making rapid actions easier to execute.

## In the game

A highly concentrated emerald liquid. It hones the drinker's quick wit and reflexes, making rapid actions easier to execute.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 3 seconds |
| Research | [Elixir of Alacrity](tech-swiftness_potion.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 1 |
| [Shadowfern Frond](item-shadowfern.md) | 1 |
| [Brambleshoot](item-brambleshoot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Elixir of Alacrity](item-swiftness_potion.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1),\n\t\t\t\tnew CraftingReagent(\"shadowfern\", 1),\n\t\t\t\tnew CraftingReagent(\"brambleshoot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"swiftness_potion\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:165`
- `Assets.Source.Items/CraftingRecipe.cs:1`
