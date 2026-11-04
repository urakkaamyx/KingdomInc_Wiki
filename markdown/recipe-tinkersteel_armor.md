# Tinkersteel Armor recipe

The mago-tech folded into this armor serve to deflect blows and dampen impacts.

## In the game

The mago-tech folded into this armor serve to deflect blows and dampen impacts.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 6 seconds |
| Research | [Tinkersteel Armor](tech-tinkersteel_armor.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 3 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Armor](item-tinkersteel_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[1]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 3)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tinkersteel_armor\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:231`
- `Assets.Source.Items/CraftingRecipe.cs:1`
