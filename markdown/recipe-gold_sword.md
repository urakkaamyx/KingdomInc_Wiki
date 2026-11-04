# Ceremonial Sword recipe

Not a suitable combat weapon as-is, but its brilliant shine will surely draw attention.

## In the game

Not a suitable combat weapon as-is, but its brilliant shine will surely draw attention.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3.5 seconds |
| Research | [Ceremonial Sword](tech-gold_sword.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 3 |
| [Iron Ingot](item-iron_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ceremonial Sword](item-gold_sword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 3),\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gold_sword\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:113`
- `Assets.Source.Items/CraftingRecipe.cs:1`
