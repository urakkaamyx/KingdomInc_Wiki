# Unlife Staff recipe

A mockery of the natural world. Demonic vines shoot out to entrap the wielder's foes, forcing them to bow in submission.

## In the game

A mockery of the natural world. Demonic vines shoot out to entrap the wielder's foes, forcing them to bow in submission.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Shrine](building-Shrine.md) |
| Base crafting time | 7.5 seconds |
| Research | [Unlife Staff](tech-unlife_staff.md) |
| Currency consumed per batch | 140 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Archbishop's Staff](item-archbishop_staff.md) | 1 |
| [Purified Mago-tech](item-purified_tech.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Unlife Staff](item-unlife_staff.md) | 1 |

## Special processing

This recipe runs additional completion logic. Consult its implementation fields and the relevant system guide; listed ingredients and results alone do not describe every effect.

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "3f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"archbishop_staff\", 1),\n\t\t\t\tnew CraftingReagent(\"purified_tech\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection(Currency.Faith, 140L)",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"unlife_staff\", 1)\n\t\t\t}",
  "OnFinished": "(CraftingInput ci) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"UpgradeWeapon\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Shrine.cs:335`
- `Assets.Source.Items/CraftingRecipe.cs:1`
