# Initiate's Staff recipe

Initiate wizards are given a staff during their training, adding their own magic over time.

## In the game

Initiate wizards are given a staff during their training, adding their own magic over time.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 3.5 seconds |
| Research | [Initiate's Staff](tech-initiate_staff.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Softwood Plank](item-wood_plank.md) | 3 |
| [Sapphire](item-sapphire.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Initiate's Staff](item-initiate_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"wood_plank\", 3),\n\t\t\t\tnew CraftingReagent(\"sapphire\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"initiate_staff\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:22`
- `Assets.Source.Items/CraftingRecipe.cs:1`
