# Gizmo recipe

A strange mago-technical innovation.

## In the game

A strange mago-technical innovation.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 1.5 seconds |
| Research | [Gizmo](tech-gizmo.md) |
| Currency consumed per batch | 22 Ingenuity |

## Ingredients

No item ingredients in the declared array. Currency costs and custom callbacks can still apply.

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Gizmo](item-gizmo.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[0]",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 22L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gizmo\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:43`
- `Assets.Source.Items/CraftingRecipe.cs:1`
