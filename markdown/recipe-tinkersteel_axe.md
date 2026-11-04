# Tinkersteel Battleaxe recipe

The weapon's mass appears to increase significantly before impact, inflicting both slashing and bludgeoning mayhem.

## In the game

The weapon's mass appears to increase significantly before impact, inflicting both slashing and bludgeoning mayhem.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 9 seconds |
| Research | [Tinkersteel Battleaxe](tech-tinkersteel_axe.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 3 |
| [Petrified Wood](item-petrified_wood.md) | 2 |
| [Primal String](item-primal_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Battleaxe](item-tinkersteel_axe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 3),\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 2),\n\t\t\t\tnew CraftingReagent(\"primal_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tinkersteel_axe\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:315`
- `Assets.Source.Items/CraftingRecipe.cs:1`
