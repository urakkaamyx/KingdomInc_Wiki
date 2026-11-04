# Blighted Dagger recipe

A system of hollow tubes constantly delivers a deadly mixture of flesh-devouring toxins to the tip of the blade.

## In the game

A system of hollow tubes constantly delivers a deadly mixture of flesh-devouring toxins to the tip of the blade.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 7.5 seconds |
| Research | [Blighted Dagger](tech-blighted_dagger.md) |
| Currency consumed per batch | 90 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Dagger](item-tinkersteel_dagger.md) | 1 |
| [Purified Mago-tech](item-purified_tech.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Blighted Dagger](item-blighted_dagger.md) | 1 |

## Special processing

This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel_dagger\", 1),\n\t\t\t\tnew CraftingReagent(\"purified_tech\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection(Currency.Faith, 90L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"blighted_dagger\", 1)\n\t\t\t}",
  "OnFinished": "(CraftingInput ci) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"UpgradeWeapon\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:221`
- `Assets.Source.Items/CraftingRecipe.cs:1`
