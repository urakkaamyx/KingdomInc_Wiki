# Summon Valkyrie recipe

A holy angelic warrior who smites her foes with divine fury.

## In the game

A holy angelic warrior who smites her foes with divine fury.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Summoning Circle](building-SummoningCircle.md) |
| Base crafting time | 16 seconds |
| Research | [Summon Valkyrie](tech-summon_valkyrie.md) |
| Currency consumed per batch | 290 Faith |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Parade Armor](item-gold_armor.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Valkyrie](item-valkyrie.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Description": "\"@valkyrie_desc\"",
  "IconName": "\"Icons2_164\"",
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Faith, 290L)",
  "CraftingTimeMultiplier": "8f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gold_armor\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"valkyrie\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/SummoningCircle.cs:79`
- `Assets.Source.Items/CraftingRecipe.cs:1`
