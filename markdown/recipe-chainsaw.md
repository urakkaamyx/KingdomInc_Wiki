# Chainsaw recipe

A wondrous invention driven by a mago-tech engine. Its sharp teeth cut into anything it comes into contact with, so be careful what you point it at.

## In the game

A wondrous invention driven by a mago-tech engine. Its sharp teeth cut into anything it comes into contact with, so be careful what you point it at.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 3 seconds |
| Research | [Chainsaw](tech-chainsaw.md) |
| Currency consumed per batch | 56 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 2 |
| [Gizmo](item-gizmo.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Chainsaw](item-chainsaw.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 56L)",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 2),\n\t\t\t\tnew CraftingReagent(\"gizmo\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"chainsaw\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:209`
- `Assets.Source.Items/CraftingRecipe.cs:1`
