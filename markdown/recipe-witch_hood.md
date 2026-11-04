# Witch Hood recipe

The living cloth whispers impossible promises and mad prophecies to the wearer.

## In the game

The living cloth whispers impossible promises and mad prophecies to the wearer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Tailor](building-Tailor.md) |
| Base crafting time | 3 seconds |
| Research | [Witch Hood](tech-witch_hood.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Witchcloth](item-witchcloth.md) | 2 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Witch Hood](item-witch_hood.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"witchcloth\", 2),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"witch_hood\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Tailor.cs:111`
- `Assets.Source.Items/CraftingRecipe.cs:1`
