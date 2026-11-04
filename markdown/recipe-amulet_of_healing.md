# Amulet of Vitality recipe

A brilliant red ruby pendant that invigorates the wearer.

## In the game

A brilliant red ruby pendant that invigorates the wearer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Amulet of Vitality](tech-amulet_of_healing.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ruby](item-gem_ruby.md) | 1 |
| [Empty Setting](item-gem_setting.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Amulet of Vitality](item-amulet_of_healing.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_ruby\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_setting\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"amulet_of_healing\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:225`
- `Assets.Source.Items/CraftingRecipe.cs:1`
