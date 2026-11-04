# Purified Mago-tech recipe

The clerics at the Cathedral of Saint Ilonia swear that the heretical influence has been purged from this powerful arcane technology.

## In the game

The clerics at the Cathedral of Saint Ilonia swear that the heretical influence has been purged from this powerful arcane technology.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 6 seconds |
| Research | [Purified Mago-tech](tech-purified_tech.md) |
| Currency consumed per batch | 23 Faith |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Heretic Mago-tech](item-heretic_tech.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Purified Mago-tech](item-purified_tech.md) | 1 item at 10% probability |
| [Heretic Mago-tech](item-heretic_tech.md) | 1 item at 90% probability |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons3_39\"",
  "CraftingTimeMultiplier": "3f",
  "BaseProductivity": "-999f",
  "CraftingCost": "new CurrencyCollection(Currency.Faith, 23L)",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"heretic_tech\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[2]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"purified_tech\", 0.1f),\n\t\t\t\tnew CraftingResult(\"heretic_tech\", 0.9f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:185`
- `Assets.Source.Items/CraftingRecipe.cs:1`
