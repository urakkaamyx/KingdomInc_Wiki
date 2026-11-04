# Summon Hellspawn recipe

A hulking demoning creature dredged up from the depths of the underworld.

## In the game

A hulking demoning creature dredged up from the depths of the underworld.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Summoning Circle](building-SummoningCircle.md) |
| Base crafting time | 16 seconds |
| Research | [Summon Hellspawn](tech-summon_hellspawn.md) |
| Currency consumed per batch | 680 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Topaz](item-gem_topaz.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Hellspawn](item-hellspawn.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_64\"",
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 680L)",
  "CraftingTimeMultiplier": "8f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_topaz\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"hellspawn\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/SummoningCircle.cs:22`
- `Assets.Source.Items/CraftingRecipe.cs:1`
