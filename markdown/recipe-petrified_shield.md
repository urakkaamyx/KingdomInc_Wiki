# Petrified Shield recipe

An impenetrable bulwark safeguarding the wielder and their allies.

## In the game

An impenetrable bulwark safeguarding the wielder and their allies.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 4 seconds |
| Research | [Petrified Shield](tech-petrified_shield.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Petrified Wood](item-petrified_wood.md) | 3 |
| [Tinkersteel](item-tinkersteel.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Petrified Shield](item-petrified_shield.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 3),\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"petrified_shield\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:223`
- `Assets.Source.Items/CraftingRecipe.cs:1`
