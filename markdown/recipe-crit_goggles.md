# Assassin's Goggles recipe

Automatically highlights the target's weakspots for the wearer.

A character can only benefit from a single source of Critical Hit.

## In the game

Automatically highlights the target's weakspots for the wearer.

A character can only benefit from a single source of Critical Hit.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 3 seconds |
| Research | [Assassin's Goggles](tech-crit_goggles.md) |
| Currency consumed per batch | 52 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Topaz](item-gem_topaz.md) | 2 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Assassin's Goggles](item-crit_goggles.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 52L)",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_topaz\", 2),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"crit_goggles\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:195`
- `Assets.Source.Items/CraftingRecipe.cs:1`
