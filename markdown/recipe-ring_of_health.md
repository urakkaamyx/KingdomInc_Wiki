# Ring of Health recipe

A pristine ring adorned with a robust ruby.

## In the game

A pristine ring adorned with a robust ruby.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Ring of Health](tech-ring_of_health.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ruby](item-gem_ruby.md) | 1 |
| [Empty Setting](item-gem_setting.md) | 1 |
| [Elegant Ring](item-simple_ring.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ring of Health](item-ring_of_health.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_ruby\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_setting\", 1),\n\t\t\t\tnew CraftingReagent(\"simple_ring\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ring_of_health\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:107`
- `Assets.Source.Items/CraftingRecipe.cs:1`
