# Widget recipe

A curious mechanical invention.

## In the game

A curious mechanical invention.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 1.5 seconds |
| Research | [Widget](tech-widget.md) |
| Currency consumed per batch | 28 Ingenuity |

## Ingredients

No item ingredients in the declared array. Currency costs and custom callbacks can still apply.

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Widget](item-widget.md) | 1 |

## Special processing

This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[0]",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 28L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"widget\", 1)\n\t\t\t}",
  "OnFinished": "(CraftingInput ci) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"WidgetInc\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:29`
- `Assets.Source.Items/CraftingRecipe.cs:1`
