# Archmage's Staff recipe

A high-ranking mage's beacon of authority, as well as the main source of their power.

## In the game

A high-ranking mage's beacon of authority, as well as the main source of their power.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 4 seconds |
| Research | [Archmage's Staff](tech-archmage_staff.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Petrified Wood](item-petrified_wood.md) | 3 |
| [Gold Wire](item-gold_wire.md) | 1 |
| [Ruby](item-gem_ruby.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Archmage's Staff](item-archmage_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 3),\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_ruby\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"archmage_staff\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:181`
- `Assets.Source.Items/CraftingRecipe.cs:1`
