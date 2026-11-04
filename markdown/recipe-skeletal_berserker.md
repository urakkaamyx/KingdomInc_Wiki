# Skeletal Berserker recipe

With a skeletal structure reinforced by magical metal, this warrior fearlessly rushes into battle.

## In the game

With a skeletal structure reinforced by magical metal, this warrior fearlessly rushes into battle.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Necromancer](building-Necromancer.md) |
| Base crafting time | 20 seconds |
| Research | [Skeletal Berserker](tech-skeletal_berserker.md) |
| Currency consumed per batch | 550 Mana |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Buried Remains](item-buried_remains.md) | 1 |
| [Arcanite Ingot](item-arcanium_ingot.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Skeletal Berserker](item-skeletal_berserker.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_84\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"buried_remains\", 1),\n\t\t\t\tnew CraftingReagent(\"arcanium_ingot\", 1)\n\t\t\t}",
  "CraftingCost": "new CurrencyCollection().Add(Currency.Mana, 550L)",
  "CraftingTimeMultiplier": "8f",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"skeletal_berserker\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Necromancer.cs:41`
- `Assets.Source.Items/CraftingRecipe.cs:1`
