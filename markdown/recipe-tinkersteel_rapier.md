# Tinkersteel Rapier recipe

The impossibly light blade darts through the air as if it's teleporting, slicing through its victims without slowing down.

## In the game

The impossibly light blade darts through the air as if it's teleporting, slicing through its victims without slowing down.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 7 seconds |
| Research | [Tinkersteel Rapier](tech-tinkersteel_rapier.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 2 |
| [Petrified Wood](item-petrified_wood.md) | 1 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Rapier](item-tinkersteel_rapier.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 2),\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 1),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tinkersteel_rapier\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:271`
- `Assets.Source.Items/CraftingRecipe.cs:1`
