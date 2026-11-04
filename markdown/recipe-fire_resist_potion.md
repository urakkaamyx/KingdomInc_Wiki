# Elixir of Fire Resistance recipe

A vial of swirling orange liquid. Looks like you're drinking liquid fire, but the taste is surprisingly pleasant.

## In the game

A vial of swirling orange liquid. Looks like you're drinking liquid fire, but the taste is surprisingly pleasant.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 3 seconds |
| Research | [Elixir of Fire Resistance](tech-fire_resist_potion.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 1 |
| [Soothing Herbs](item-soothing_herbs.md) | 1 |
| [Ember Briar](item-ember_briar.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Elixir of Fire Resistance](item-fire_resist_potion.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1),\n\t\t\t\tnew CraftingReagent(\"soothing_herbs\", 1),\n\t\t\t\tnew CraftingReagent(\"ember_briar\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"fire_resist_potion\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:81`
- `Assets.Source.Items/CraftingRecipe.cs:1`
