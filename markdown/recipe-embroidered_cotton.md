# Embroidered Cotton recipe

Patterned with arcane symbols and suitable for the creation of powerful equipment.

## In the game

Patterned with arcane symbols and suitable for the creation of powerful equipment.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 2.5 seconds |
| Research | [Embroidered Cotton](tech-embroidered_cotton.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Cotton Cloth](item-cotton_cloth.md) | 1 |
| [Enchanted Thread](item-enchanted_cotton_thread.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Embroidered Cotton](item-embroidered_cotton.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"cotton_cloth\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_cotton_thread\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"embroidered_cotton\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:201`
- `Assets.Source.Items/CraftingRecipe.cs:1`
