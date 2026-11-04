# Identify Gemstones recipe

Inspect ancient gemstones to determine their physical and magical characteristics.

Reminder: The Filter node can be used to disentangle the mixed output gems.

## In the game

Inspect ancient gemstones to determine their physical and magical characteristics.

Reminder: The Filter node can be used to disentangle the mixed output gems.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 2 seconds |
| Research | [Identify Gemstones](tech-identify_gem.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Gemstone](item-ancient_gem.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Emerald](item-gem_emerald.md) | 1 item at 20% probability |
| [Topaz](item-gem_topaz.md) | 1 item at 20% probability |
| [Ruby](item-gem_ruby.md) | 1 item at 20% probability |
| [Aquamarine](item-gem_aquamarine.md) | 1 item at 20% probability |
| [Diamond Chip](item-gem_diamond.md) | 1 item at 20% probability |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons_208\"",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_gem\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[5]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gem_emerald\", 0.2f),\n\t\t\t\tnew CraftingResult(\"gem_topaz\", 0.2f),\n\t\t\t\tnew CraftingResult(\"gem_ruby\", 0.2f),\n\t\t\t\tnew CraftingResult(\"gem_aquamarine\", 0.2f),\n\t\t\t\tnew CraftingResult(\"gem_diamond\", 0.2f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:8`
- `Assets.Source.Items/CraftingRecipe.cs:1`
