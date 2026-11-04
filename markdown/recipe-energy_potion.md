# Revitalizing Potion recipe

A pale yellow potion that instantly re-energizes even the most tired soul.

## In the game

A pale yellow potion that instantly re-energizes even the most tired soul.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 2.5 seconds |
| Research | [Revitalizing Potion](tech-energy_potion.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Revitalizing Potion](item-energy_potion.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"energy_potion\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:51`
- `Assets.Source.Items/CraftingRecipe.cs:1`
