# Attuned Catalyst recipe

An alchemical reagent used in a wide variety of arcane processes.

## In the game

An alchemical reagent used in a wide variety of arcane processes.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 28 seconds |
| Research | [Attuned Catalyst](tech-attuned_catalyst.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Mercurial Flux](item-mercurial_flux.md) | 20 |
| [Ancient Gemstone](item-ancient_gem.md) | 1 |
| [Crystalized Mana](item-crystal_mana.md) | 4 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Attuned Catalyst](item-attuned_catalyst.md) | 20 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"mercurial_flux\", 20),\n\t\t\t\tnew CraftingReagent(\"ancient_gem\", 1),\n\t\t\t\tnew CraftingReagent(\"crystal_mana\", 4)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"attuned_catalyst\", 20)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
