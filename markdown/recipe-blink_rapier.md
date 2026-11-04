# Ethereal Rapier recipe

The thin blade of this sword is only connected to the hilt in some unseen dimension, allowing the point to bypass armor with ease.

## In the game

The thin blade of this sword is only connected to the hilt in some unseen dimension, allowing the point to bypass armor with ease.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 7.5 seconds |
| Research | [Ethereal Rapier](tech-blink_rapier.md) |
| Currency consumed per batch | 90 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Rapier](item-tinkersteel_rapier.md) | 1 |
| [Purified Mago-tech](item-purified_tech.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ethereal Rapier](item-blink_rapier.md) | 1 |

## Special processing

This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel_rapier\", 1),\n\t\t\t\tnew CraftingReagent(\"purified_tech\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection(Currency.Faith, 90L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"blink_rapier\", 1)\n\t\t\t}",
  "OnFinished": "(CraftingInput ci) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"UpgradeWeapon\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:240`
- `Assets.Source.Items/CraftingRecipe.cs:1`
