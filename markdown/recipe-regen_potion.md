# Elixir of Regeneration recipe

The thick liquid burns on the way down, in a pleasant way. The drinker feels continuously reinvigorated, an effect that can last for days.

## In the game

The thick liquid burns on the way down, in a pleasant way. The drinker feels continuously reinvigorated, an effect that can last for days.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 3 seconds |
| Research | [Elixir of Regeneration](tech-regen_potion.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 1 |
| [Toxin Sample](item-toxin_sample.md) | 1 |
| [Soothing Herbs](item-soothing_herbs.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Elixir of Regeneration](item-regen_potion.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1),\n\t\t\t\tnew CraftingReagent(\"toxin_sample\", 1),\n\t\t\t\tnew CraftingReagent(\"soothing_herbs\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"regen_potion\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:179`
- `Assets.Source.Items/CraftingRecipe.cs:1`
