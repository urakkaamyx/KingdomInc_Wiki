# Tinkersteel Helm recipe

The continuous clicking of tiny gears slowly drives the wearer insane, but also serves to keep them focused.

## In the game

The continuous clicking of tiny gears slowly drives the wearer insane, but also serves to keep them focused.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 5 seconds |
| Research | [Tinkersteel Helm](tech-tinkersteel_helm.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Helm](item-tinkersteel_helm.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tinkersteel_helm\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:244`
- `Assets.Source.Items/CraftingRecipe.cs:1`
