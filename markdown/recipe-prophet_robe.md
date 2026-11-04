# Dark Prophet's Robe recipe

A beguiling aura draws the attention of allies and foes alike, turning even the most hardened skeptic into a devout follower.

## In the game

A beguiling aura draws the attention of allies and foes alike, turning even the most hardened skeptic into a devout follower.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 7.5 seconds |
| Research | [Dark Prophet's Robe](tech-prophet_robe.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Witch Robe](item-witch_robe.md) | 1 |
| [Decoded Writings](item-decoded_writings.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Dark Prophet's Robe](item-prophet_robe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"witch_robe\", 1),\n\t\t\t\tnew CraftingReagent(\"decoded_writings\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"prophet_robe\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:359`
- `Assets.Source.Items/CraftingRecipe.cs:1`
