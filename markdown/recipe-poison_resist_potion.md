# Elixir of Poison Resistance recipe

A sickly-green potion. Drinking it makes you gag at first, before that nagging headache miraculously disappears.

## In the game

A sickly-green potion. Drinking it makes you gag at first, before that nagging headache miraculously disappears.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 3 seconds |
| Research | [Elixir of Poison Resistance](tech-poison_resist_potion.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 1 |
| [Soothing Herbs](item-soothing_herbs.md) | 1 |
| [Bogberry Branch](item-bogberry_branch.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Elixir of Poison Resistance](item-poison_resist_potion.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1),\n\t\t\t\tnew CraftingReagent(\"soothing_herbs\", 1),\n\t\t\t\tnew CraftingReagent(\"bogberry_branch\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"poison_resist_potion\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:109`
- `Assets.Source.Items/CraftingRecipe.cs:1`
