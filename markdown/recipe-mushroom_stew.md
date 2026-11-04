# Mushroom Stew recipe

A hearty stew that fortifies both body and mind. Overconsumption may lead to hallucinations.

## In the game

A hearty stew that fortifies both body and mind. Overconsumption may lead to hallucinations.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Campfire](building-Campfire.md) |
| Base crafting time | 5 seconds |
| Research | [Mushroom Stew](tech-mushroom_stew.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Mushroom](item-mushroom.md) | 1 |
| [Bone](item-bone.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Mushroom Stew](item-mushroom_stew.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "ValueMultiplier": "2.0",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"mushroom\", 1),\n\t\t\t\tnew CraftingReagent(\"bone\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"mushroom_stew\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Campfire.cs:51`
- `Assets.Source.Items/CraftingRecipe.cs:1`
