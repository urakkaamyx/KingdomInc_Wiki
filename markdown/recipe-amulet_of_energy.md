# Amulet of Vigor recipe

Energizes the wearer and anyone in their vicinity.

## In the game

Energizes the wearer and anyone in their vicinity.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Amulet of Vigor](tech-amulet_of_energy.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Eye of the Watcher](item-observer_eye.md) | 1 |
| [Empty Setting](item-gem_setting.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Amulet of Vigor](item-amulet_of_energy.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"observer_eye\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_setting\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"amulet_of_energy\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:239`
- `Assets.Source.Items/CraftingRecipe.cs:1`
