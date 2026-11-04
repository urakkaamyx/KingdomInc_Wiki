# Gold Wire recipe

Finely spun gold wire, used in the creation of detailed engraving patterns.

## In the game

Finely spun gold wire, used in the creation of detailed engraving patterns.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 2 seconds |
| Research | [Gold Wire](tech-gold_wire.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Gold Wire](item-gold_wire.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gold_wire\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:14`
- `Assets.Source.Items/CraftingRecipe.cs:1`
