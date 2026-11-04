# Golem Gauntlets recipe

Enhances the wearer's natural strength, allowing them to lift heavy boulders with ease.

## In the game

Enhances the wearer's natural strength, allowing them to lift heavy boulders with ease.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 2.5 seconds |
| Research | [Golem Gauntlets](tech-golem_gauntlets.md) |
| Currency consumed per batch | 39 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 1 |
| [Doodad](item-doodad.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Golem Gauntlets](item-golem_gauntlets.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 39L)",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 1),\n\t\t\t\tnew CraftingReagent(\"doodad\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"golem_gauntlets\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:167`
- `Assets.Source.Items/CraftingRecipe.cs:1`
