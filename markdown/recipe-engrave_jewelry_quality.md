# Engraved Jewelry recipe

A simple but delicate engraving of power that gives a small quality boost.

## In the game

A simple but delicate engraving of power that gives a small quality boost.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 9 seconds |
| Research | [Engraved Jewelry](tech-engrave_jewelry_quality.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Jewelry (any) | 1 |
| [Gold Wire](item-gold_wire.md) | 1 |
| [Silver Thread](item-silver_thread.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Engraved Jewelry](enhancement-engrave_jewelry_quality.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_98\"",
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tcraftingReagent4,\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 1),\n\t\t\t\tnew CraftingReagent(\"silver_thread\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_jewelry_quality\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:227`
- `Assets.Source.Items/CraftingRecipe.cs:1`
