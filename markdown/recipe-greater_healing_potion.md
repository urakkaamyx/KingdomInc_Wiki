# Greater Healing Potion recipe

A brilliant red potion that can instantly restore grievous wounds.

## In the game

A brilliant red potion that can instantly restore grievous wounds.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 3 seconds |
| Research | [Greater Healing Potion](tech-greater_healing_potion.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 1 |
| [Moonberry](item-moonberry.md) | 1 |
| [Ember Briar](item-ember_briar.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Greater Healing Potion](item-greater_healing_potion.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"glass_vial\", 1),\n\t\t\t\tnew CraftingReagent(\"moonberry\", 1),\n\t\t\t\tnew CraftingReagent(\"ember_briar\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"greater_healing_potion\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:137`
- `Assets.Source.Items/CraftingRecipe.cs:1`
