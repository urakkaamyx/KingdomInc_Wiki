# Healing Potion recipe

A brilliant red potion that can instantly restore minor wounds.

## In the game

A brilliant red potion that can instantly restore minor wounds.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 2.5 seconds |
| Research | [Healing Potion](tech-healing_potion.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 1 |
| [Soothing Herbs](item-soothing_herbs.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Healing Potion](item-healing_potion.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1),\n\t\t\t\tnew CraftingReagent(\"soothing_herbs\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"healing_potion\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:38`
- `Assets.Source.Items/CraftingRecipe.cs:1`
