# Petrified Wood recipe

A revolutionary new way to incorporate cutting edge mago-tech into traditional craftsmanship.

## In the game

A revolutionary new way to incorporate cutting edge mago-tech into traditional craftsmanship.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 3 seconds |
| Research | [Petrified Wood](tech-petrified_wood.md) |
| Currency consumed per batch | 4 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Resin](item-resin.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |
| [Ancient Wood Plank](item-ancient_wood_plank.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Petrified Wood](item-petrified_wood.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 4L)",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"resin\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1),\n\t\t\t\tnew CraftingReagent(\"ancient_wood_plank\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"petrified_wood\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:138`
- `Assets.Source.Items/CraftingRecipe.cs:1`
