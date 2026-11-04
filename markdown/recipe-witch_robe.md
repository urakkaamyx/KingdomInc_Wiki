# Witch Robe recipe

An unworthy wearer will slowly have their soul siphoned away by the living fabric until nothing is left.

## In the game

An unworthy wearer will slowly have their soul siphoned away by the living fabric until nothing is left.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 3.5 seconds |
| Research | [Witch Robe](tech-witch_robe.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Witchcloth](item-witchcloth.md) | 3 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Witch Robe](item-witch_robe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"witchcloth\", 3),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"witch_robe\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:98`
- `Assets.Source.Items/CraftingRecipe.cs:1`
