# Crystalline Staff recipe

A solid wood staff adorned with fragmented mana crystals and delicate gold detailing.

## In the game

A solid wood staff adorned with fragmented mana crystals and delicate gold detailing.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Carpenter](building-Carpenter.md) |
| Base crafting time | 3 seconds |
| Research | [Crystalline Staff](tech-ancient_int_staff.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Ancient Wood Staff](item-ancient_wood_staff.md) | 1 |
| [Crystalized Mana](item-crystal_mana.md) | 1 |
| [Gold Wire](item-gold_wire.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Crystalline Staff](item-ancient_int_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"ancient_wood_staff\", 1),\n\t\t\t\tnew CraftingReagent(\"crystal_mana\", 1),\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ancient_int_staff\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Carpenter.cs:126`
- `Assets.Source.Items/CraftingRecipe.cs:1`
