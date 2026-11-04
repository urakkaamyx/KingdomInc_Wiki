# Trueshot Bow recipe

Fired arrows correct themselves in midair to pierce the enemy's weakspots every single time.

## In the game

Fired arrows correct themselves in midair to pierce the enemy's weakspots every single time.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 3.5 seconds |
| Research | [Trueshot Bow](tech-trueshot_bow.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Petrified Wood](item-petrified_wood.md) | 2 |
| [Tinkersteel](item-tinkersteel.md) | 1 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Trueshot Bow](item-trueshot_bow.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 2),\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 1),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"trueshot_bow\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:209`
- `Assets.Source.Items/CraftingRecipe.cs:1`
