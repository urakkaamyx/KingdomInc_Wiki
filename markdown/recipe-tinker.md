# Tinker recipe

Experiment with a variety of base components to create all-new inventions and generate Ingenuity.

## In the game

Experiment with a variety of base components to create all-new inventions and generate Ingenuity.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 6 seconds |
| Research | [Tinker](tech-tinker.md) |
| Currency reward per batch | 12 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Ingot](item-arcanium_ingot.md) | 1 |
| [Crystalized Mana](item-crystal_mana.md) | 1 |
| [Attuned Catalyst](item-attuned_catalyst.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Widget](item-widget.md) | 1 item at 33.33% probability |
| [Gizmo](item-gizmo.md) | 1 item at 33.33% probability |
| [Doodad](item-doodad.md) | 1 item at 33.33% probability |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons2_94\"",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 1),\n\t\t\t\tnew CraftingReagent(\"crystal_mana\", 1),\n\t\t\t\tnew CraftingReagent(\"attuned_catalyst\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[3]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"widget\", 0.3333f),\n\t\t\t\tnew CraftingResult(\"gizmo\", 0.3333f),\n\t\t\t\tnew CraftingResult(\"doodad\", 0.3333f)\n\t\t\t}",
  "CraftingReward": "new CurrencyCollection(Currency.Ingenuity, 12L)"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:10`
- `Assets.Source.Items/CraftingRecipe.cs:1`
