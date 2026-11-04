# Winged Boots recipe

A wondrous invention that allows the wearer to fly over short distances, making feats of dexterity more manageable.

## In the game

A wondrous invention that allows the wearer to fly over short distances, making feats of dexterity more manageable.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 2.5 seconds |
| Research | [Winged Boots](tech-winged_boots.md) |
| Currency consumed per batch | 41 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Primal Leather](item-primal_leather.md) | 1 |
| [Widget](item-widget.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Winged Boots](item-winged_boots.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 41L)",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"primal_leather\", 1),\n\t\t\t\tnew CraftingReagent(\"widget\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"winged_boots\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:153`
- `Assets.Source.Items/CraftingRecipe.cs:1`
