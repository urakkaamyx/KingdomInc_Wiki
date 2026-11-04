# Medallion of Excellence recipe

A talisman normally awarded to exceptionally gifted adventurers after a lifetime of service to the guild.

## In the game

A talisman normally awarded to exceptionally gifted adventurers after a lifetime of service to the guild.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Medallion of Excellence](tech-stats_amulet.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Aquamarine](item-gem_aquamarine.md) | 1 |
| [Empty Setting](item-gem_setting.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Medallion of Excellence](item-stats_amulet.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_aquamarine\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_setting\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"stats_amulet\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:323`
- `Assets.Source.Items/CraftingRecipe.cs:1`
