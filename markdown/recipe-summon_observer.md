# Summon Watcher recipe

An ominous floating creature that attacks enemies from afar using its chaotic eyebeams.

## In the game

An ominous floating creature that attacks enemies from afar using its chaotic eyebeams.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Summoning Circle](building-SummoningCircle.md) |
| Base crafting time | 16 seconds |
| Research | [Summon Watcher](tech-summon_observer.md) |
| Currency consumed per batch | 390 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Eye of the Watcher](item-observer_eye.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Watcher](item-observer.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_162\"",
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 390L)",
  "CraftingTimeMultiplier": "8f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"observer_eye\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"observer\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/SummoningCircle.cs:37`
- `Assets.Source.Items/CraftingRecipe.cs:1`
