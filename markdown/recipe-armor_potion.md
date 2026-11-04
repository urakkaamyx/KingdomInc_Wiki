# Stoneskin Elixir recipe

A disgustingly bitter potion. Shortly after consumption, the drinker feels impervious to harm.

## In the game

A disgustingly bitter potion. Shortly after consumption, the drinker feels impervious to harm.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 3 seconds |
| Research | [Stoneskin Elixir](tech-armor_potion.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 1 |
| [Brambleshoot](item-brambleshoot.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Stoneskin Elixir](item-armor_potion.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1),\n\t\t\t\tnew CraftingReagent(\"brambleshoot\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"armor_potion\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:123`
- `Assets.Source.Items/CraftingRecipe.cs:1`
