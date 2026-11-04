# Arcanite Casque recipe

A helmet fit for a champion.

## In the game

A helmet fit for a champion.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 2.5 seconds |
| Research | [Arcanite Casque](tech-arcanium_helm.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Ingot](item-arcanium_ingot.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Casque](item-arcanium_helm.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"arcanium_helm\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:165`
- `Assets.Source.Items/CraftingRecipe.cs:1`
