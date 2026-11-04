# Lifebloom Amulet recipe

Exudes a gentle soothing aura that intermittently heals the wearer's allies for a small amount.

## In the game

Exudes a gentle soothing aura that intermittently heals the wearer's allies for a small amount.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Lifebloom Amulet](tech-lifebloom_amulet.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Emerald](item-gem_emerald.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Lifebloom Amulet](item-lifebloom_amulet.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_emerald\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"lifebloom_amulet\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:295`
- `Assets.Source.Items/CraftingRecipe.cs:1`
