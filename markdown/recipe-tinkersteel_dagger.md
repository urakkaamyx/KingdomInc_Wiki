# Tinkersteel Dagger recipe

A nimble, telescopic blade. The blade extends after puncturing the target, causing extensive internal damage.

## In the game

A nimble, telescopic blade. The blade extends after puncturing the target, causing extensive internal damage.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 6 seconds |
| Research | [Tinkersteel Dagger](tech-tinkersteel_dagger.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 2 |
| [Petrified Wood](item-petrified_wood.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Dagger](item-tinkersteel_dagger.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 2),\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tinkersteel_dagger\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:286`
- `Assets.Source.Items/CraftingRecipe.cs:1`
