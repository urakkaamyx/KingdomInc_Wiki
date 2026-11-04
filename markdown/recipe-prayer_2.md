# Ritual Prayer recipe

A more powerful prayer that would be more likely to garner Saint Ilonia's favor.

## In the game

A more powerful prayer that would be more likely to garner Saint Ilonia's favor.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 15 seconds |
| Research | [Ritual Prayer](tech-prayer_2.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Cleric | 1 |
| [Blessed Prayer Beads](item-blessed_prayer_beads.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| Custom selection | OutputCleric(0.3f) |
| Custom selection | OutputFaith(214f) |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons3_73\"",
  "BaseProductivity": "-999f",
  "CraftingTimeMultiplier": "6f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tcraftingReagent,\n\t\t\t\tnew CraftingReagent(\"blessed_prayer_beads\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[2]\n\t\t\t{\n\t\t\t\tOutputCleric(0.3f),\n\t\t\t\tOutputFaith(214f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:46`
- `Assets.Source.Items/CraftingRecipe.cs:1`
