# Identify Plants recipe

Your expert alchemist takes a good look at the plant samples collected by your adventurers and sorts them by type.

## In the game

Your expert alchemist takes a good look at the plant samples collected by your adventurers and sorts them by type.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Alchemist](building-Alchemist.md) |
| Base crafting time | 2 seconds |
| Research | [Identify Plants](tech-identify_plants.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Unidentified Plants](item-unidentified_plants.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Brambleshoot](item-brambleshoot.md) | 1 item at 20% probability |
| [Ember Briar](item-ember_briar.md) | 1 item at 20% probability |
| [Bogberry Branch](item-bogberry_branch.md) | 1 item at 20% probability |
| [Shadowfern Frond](item-shadowfern.md) | 1 item at 20% probability |
| [Moonberry](item-moonberry.md) | 1 item at 20% probability |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons2_148\"",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"unidentified_plants\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[5]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"brambleshoot\", 0.2f),\n\t\t\t\tnew CraftingResult(\"ember_briar\", 0.2f),\n\t\t\t\tnew CraftingResult(\"bogberry_branch\", 0.2f),\n\t\t\t\tnew CraftingResult(\"shadowfern\", 0.2f),\n\t\t\t\tnew CraftingResult(\"moonberry\", 0.2f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Alchemist.cs:64`
- `Assets.Source.Items/CraftingRecipe.cs:1`
