# Reinforced Wooden Shield recipe

The iron borders of this shield will keep it together long enough for the bearer to stand a chance in open combat.

## In the game

The iron borders of this shield will keep it together long enough for the bearer to stand a chance in open combat.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 2.5 seconds |
| Research | [Reinforced Wooden Shield](tech-reinforced_wooden_shield.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Simple Wooden Shield](item-simple_wooden_shield.md) | 1 |
| [Iron Ingot](item-iron_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Reinforced Wooden Shield](item-reinforced_wooden_shield.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"simple_wooden_shield\", 1),\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"reinforced_wooden_shield\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:60`
- `Assets.Source.Items/CraftingRecipe.cs:1`
