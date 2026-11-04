# Ring of Wisdom recipe

A graceful ring adorned with a majestic diamond.

## In the game

A graceful ring adorned with a majestic diamond.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Ring of Wisdom](tech-ring_of_wisdom.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Diamond Chip](item-gem_diamond.md) | 1 |
| [Empty Setting](item-gem_setting.md) | 1 |
| [Elegant Ring](item-simple_ring.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ring of Wisdom](item-ring_of_wisdom.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_diamond\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_setting\", 1),\n\t\t\t\tnew CraftingReagent(\"simple_ring\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ring_of_wisdom\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:93`
- `Assets.Source.Items/CraftingRecipe.cs:1`
