# Rough Vest recipe

The durable leather hide, while low quality, provides adequate protection in combat.

## In the game

The durable leather hide, while low quality, provides adequate protection in combat.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Leatherworker](building-Leatherworker.md) |
| Base crafting time | 3 seconds |
| Research | [Rough Vest](tech-rough_vest.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Rough Leather](item-rough_leather.md) | 3 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Rough Vest](item-rough_vest.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"rough_leather\", 3)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"rough_vest\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Leatherworker.cs:20`
- `Assets.Source.Items/CraftingRecipe.cs:1`
