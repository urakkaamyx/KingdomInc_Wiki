# Triune Protector recipe

A portable anti-magic shield that protects the wearer from Fire, Shadow and Poison damage all at the same time.

## In the game

A portable anti-magic shield that protects the wearer from Fire, Shadow and Poison damage all at the same time.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 2.5 seconds |
| Research | [Triune Protector](tech-triune_shield.md) |
| Currency consumed per batch | 46 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 1 |
| [Petrified Wood](item-petrified_wood.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Triune Protector](item-triune_shield.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 46L)",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 1),\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"triune_shield\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:237`
- `Assets.Source.Items/CraftingRecipe.cs:1`
