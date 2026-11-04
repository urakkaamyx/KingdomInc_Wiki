# Iron Rapier recipe

A nimble blade designed for dueling. Its decorative bone crossguard is reinforced to protect the wielder's hand.

## In the game

A nimble blade designed for dueling. Its decorative bone crossguard is reinforced to protect the wielder's hand.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 4 seconds |
| Research | [Iron Rapier](tech-iron_rapier.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Iron Ingot](item-iron_ingot.md) | 3 |
| [Bone](item-bone.md) | 1 |
| [Resin](item-resin.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Iron Rapier](item-iron_rapier.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"iron_ingot\", 3),\n\t\t\t\tnew CraftingReagent(\"bone\", 1),\n\t\t\t\tnew CraftingReagent(\"resin\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"iron_rapier\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:126`
- `Assets.Source.Items/CraftingRecipe.cs:1`
