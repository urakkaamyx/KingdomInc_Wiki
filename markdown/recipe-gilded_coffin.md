# Gilded Coffin recipe

A wooden coffin decorated with a copious amount of gold, destined to hold the remains of someone important.

## In the game

A wooden coffin decorated with a copious amount of gold, destined to hold the remains of someone important.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3 seconds |
| Research | [Gilded Coffin](tech-gilded_coffin.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Coffin](item-coffin.md) | 1 |
| [Gold Wire](item-gold_wire.md) | 1 |
| [Gold Ingot](item-gold_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Gilded Coffin](item-gilded_coffin.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"coffin\", 1),\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 1),\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gilded_coffin\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:243`
- `Assets.Source.Items/CraftingRecipe.cs:1`
