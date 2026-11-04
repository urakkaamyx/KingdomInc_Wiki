# Arcanite Chestguard recipe

If you're going into battle, you might as well do it in style.

## In the game

If you're going into battle, you might as well do it in style.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3 seconds |
| Research | [Arcanite Chestguard](tech-arcanium_armor.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Ingot](item-arcanium_ingot.md) | 3 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Arcanite Chestguard](item-arcanium_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 3)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"arcanium_armor\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:153`
- `Assets.Source.Items/CraftingRecipe.cs:1`
