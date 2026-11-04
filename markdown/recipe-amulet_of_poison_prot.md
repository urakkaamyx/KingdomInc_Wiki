# Panacea Amulet recipe

Creates a detoxifying aura that protects the wearer and their allies from even the most vile poisons.

## In the game

Creates a detoxifying aura that protects the wearer and their allies from even the most vile poisons.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Panacea Amulet](tech-amulet_of_poison_prot.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Toxin Sample](item-toxin_sample.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Panacea Amulet](item-amulet_of_poison_prot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"toxin_sample\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"amulet_of_poison_prot\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:281`
- `Assets.Source.Items/CraftingRecipe.cs:1`
