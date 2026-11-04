# Ring of Dexterity recipe

An elegant ring adorned with a shifting emerald.

## In the game

An elegant ring adorned with a shifting emerald.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Ring of Dexterity](tech-ring_of_dexterity.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Emerald](item-gem_emerald.md) | 1 |
| [Empty Setting](item-gem_setting.md) | 1 |
| [Elegant Ring](item-simple_ring.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ring of Dexterity](item-ring_of_dexterity.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_emerald\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_setting\", 1),\n\t\t\t\tnew CraftingReagent(\"simple_ring\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ring_of_dexterity\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:65`
- `Assets.Source.Items/CraftingRecipe.cs:1`
