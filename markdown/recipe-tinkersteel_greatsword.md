# Tinkersteel Greatsword recipe

Even though the edge doesn't seem to be particularly sharp, it still slices through almost anything with ease.

## In the game

Even though the edge doesn't seem to be particularly sharp, it still slices through almost anything with ease.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 9 seconds |
| Research | [Tinkersteel Greatsword](tech-tinkersteel_greatsword.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 4 |
| [Petrified Wood](item-petrified_wood.md) | 1 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Greatsword](item-tinkersteel_greatsword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 4),\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 1),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tinkersteel_greatsword\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:300`
- `Assets.Source.Items/CraftingRecipe.cs:1`
