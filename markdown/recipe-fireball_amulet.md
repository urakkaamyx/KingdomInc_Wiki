# Necklace of Fireballs recipe

The tiny beads on this necklace are, in fact, dangerous weapons: They spontaneously combust after being thrown.

## In the game

The tiny beads on this necklace are, in fact, dangerous weapons: They spontaneously combust after being thrown.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Necklace of Fireballs](tech-fireball_amulet.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Topaz](item-gem_topaz.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Necklace of Fireballs](item-fireball_amulet.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_topaz\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"fireball_amulet\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:309`
- `Assets.Source.Items/CraftingRecipe.cs:1`
