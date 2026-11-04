# Blessed Prayer Beads recipe

Having been blessed by a miracle of Saint Ilonia, clerics from all walks of life would be honored to own these beads.

## In the game

Having been blessed by a miracle of Saint Ilonia, clerics from all walks of life would be honored to own these beads.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 2 seconds |
| Research | [Blessed Prayer Beads](tech-blessed_prayer_beads.md) |
| Currency consumed per batch | 84 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Prayer Beads](item-prayer_beads.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Blessed Prayer Beads](item-blessed_prayer_beads.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Faith, 84L)",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"prayer_beads\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"blessed_prayer_beads\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:33`
- `Assets.Source.Items/CraftingRecipe.cs:1`
