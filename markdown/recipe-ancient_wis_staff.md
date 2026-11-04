# Staff of Sages recipe

A runecarved staff of ancient design, carried by sages and soothsayers for generations.

## In the game

A runecarved staff of ancient design, carried by sages and soothsayers for generations.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 3 seconds |
| Research | [Staff of Sages](tech-ancient_wis_staff.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Staff](item-ancient_wood_staff.md) | 1 |
| [Ancient Gemstone](item-ancient_gem.md) | 1 |
| [Silver Thread](item-silver_thread.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Staff of Sages](item-ancient_wis_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_wood_staff\", 1),\n\t\t\t\tnew CraftingReagent(\"ancient_gem\", 1),\n\t\t\t\tnew CraftingReagent(\"silver_thread\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ancient_wis_staff\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:140`
- `Assets.Source.Items/CraftingRecipe.cs:1`
