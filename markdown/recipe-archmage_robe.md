# Archmage's Robe recipe

Stylish and gaudy, this magnificent robe is sure to awe anyone that sees you wearing it. No harm ever came from trying on some clothes, right?

## In the game

Stylish and gaudy, this magnificent robe is sure to awe anyone that sees you wearing it. No harm ever came from trying on some clothes, right?

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 7.5 seconds |
| Research | [Archmage's Robe](tech-archmage_robe.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Witch Robe](item-witch_robe.md) | 1 |
| [Decoded Writings](item-decoded_writings.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Archmage's Robe](item-archmage_robe.md) | 1 |

## Special processing

This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"witch_robe\", 1),\n\t\t\t\tnew CraftingReagent(\"decoded_writings\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"archmage_robe\", 1)\n\t\t\t}",
  "OnFinished": "(CraftingInput ci) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"UpgradeArmor\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:327`
- `Assets.Source.Items/CraftingRecipe.cs:1`
