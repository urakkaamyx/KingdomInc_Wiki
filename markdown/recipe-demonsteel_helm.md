# Demonsteel Helm recipe

The incessant clicking of gears has been replaced with maddening whispers.

## In the game

The incessant clicking of gears has been replaced with maddening whispers.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 7.5 seconds |
| Research | [Demonsteel Helm](tech-demonsteel_helm.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Helm](item-tinkersteel_helm.md) | 1 |
| [Decoded Writings](item-decoded_writings.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Demonsteel Helm](item-demonsteel_helm.md) | 1 |

## Special processing

This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel_helm\", 1),\n\t\t\t\tnew CraftingReagent(\"decoded_writings\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"demonsteel_helm\", 1)\n\t\t\t}",
  "OnFinished": "(CraftingInput ci) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"UpgradeArmor\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:219`
- `Assets.Source.Items/CraftingRecipe.cs:1`
