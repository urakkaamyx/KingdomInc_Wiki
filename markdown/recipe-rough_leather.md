# Rough Leather recipe

Processed skin of a dead animal with surprisingly many use cases.

## In the game

Processed skin of a dead animal with surprisingly many use cases.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 2 seconds |
| Research | [Rough Leather](tech-rough_leather.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Wolf Hide](item-wolf_hide.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Rough Leather](item-rough_leather.md) | 2 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"wolf_hide\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"rough_leather\", 2)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:44`
- `Assets.Source.Items/CraftingRecipe.cs:1`
