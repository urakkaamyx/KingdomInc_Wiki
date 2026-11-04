# Leyline Goggles recipe

Allows the wearer to detect and identify subtle magical influences embedded in the environment.

## In the game

Allows the wearer to detect and identify subtle magical influences embedded in the environment.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 3 seconds |
| Research | [Leyline Goggles](tech-mind_goggles.md) |
| Currency consumed per batch | 36 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Aquamarine](item-gem_aquamarine.md) | 2 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Leyline Goggles](item-mind_goggles.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 36L)",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_aquamarine\", 2),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"mind_goggles\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:181`
- `Assets.Source.Items/CraftingRecipe.cs:1`
