# Archbishop's Staff recipe

An honorable weapon of the high clergy. Its overwhelming presence demands both reverence and obedience.

## In the game

An honorable weapon of the high clergy. Its overwhelming presence demands both reverence and obedience.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 4 seconds |
| Research | [Archbishop's Staff](tech-archbishop_staff.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Petrified Wood](item-petrified_wood.md) | 3 |
| [Silver Thread](item-silver_thread.md) | 1 |
| [Diamond Chip](item-gem_diamond.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Archbishop's Staff](item-archbishop_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 3),\n\t\t\t\tnew CraftingReagent(\"silver_thread\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_diamond\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"archbishop_staff\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:195`
- `Assets.Source.Items/CraftingRecipe.cs:1`
