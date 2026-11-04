# Possessed Shield recipe

The demonic creature trapped inside the shield threatens to curse anyone that dares to strike it.

## In the game

The demonic creature trapped inside the shield threatens to curse anyone that dares to strike it.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 7.5 seconds |
| Research | [Possessed Shield](tech-infected_shield.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Petrified Shield](item-petrified_shield.md) | 1 |
| [Decoded Writings](item-decoded_writings.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Possessed Shield](item-infected_shield.md) | 1 |

## Special processing

This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"petrified_shield\", 1),\n\t\t\t\tnew CraftingReagent(\"decoded_writings\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"infected_shield\", 1)\n\t\t\t}",
  "OnFinished": "(CraftingInput ci) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"UpgradeArmor\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:255`
- `Assets.Source.Items/CraftingRecipe.cs:1`
