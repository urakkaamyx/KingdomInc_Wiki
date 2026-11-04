# Dark Prophet's Hood recipe

The wearer is tormented by myriad voices screaming blasphemous prophecies into their ears.

## In the game

The wearer is tormented by myriad voices screaming blasphemous prophecies into their ears.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 7.5 seconds |
| Research | [Dark Prophet's Hood](tech-prophet_hood.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Witch Hood](item-witch_hood.md) | 1 |
| [Decoded Writings](item-decoded_writings.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Dark Prophet's Hood](item-prophet_hood.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"witch_hood\", 1),\n\t\t\t\tnew CraftingReagent(\"decoded_writings\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"prophet_hood\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:345`
- `Assets.Source.Items/CraftingRecipe.cs:1`
