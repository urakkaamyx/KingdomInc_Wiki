# Demonsteel Armor recipe

Blood drips continuously from tiny holes in the armor's surface with no indication of where it's coming from.

## In the game

Blood drips continuously from tiny holes in the armor's surface with no indication of where it's coming from.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 7.5 seconds |
| Research | [Demonsteel Armor](tech-demonsteel_armor.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Armor](item-tinkersteel_armor.md) | 1 |
| [Decoded Writings](item-decoded_writings.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Demonsteel Armor](item-demonsteel_armor.md) | 1 |

## Special processing

This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel_armor\", 1),\n\t\t\t\tnew CraftingReagent(\"decoded_writings\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"demonsteel_armor\", 1)\n\t\t\t}",
  "OnFinished": "(CraftingInput ci) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"UpgradeArmor\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:237`
- `Assets.Source.Items/CraftingRecipe.cs:1`
