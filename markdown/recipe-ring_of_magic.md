# Ring of Magic recipe

A powerful ring adorned with a brilliant aquamarine.

## In the game

A powerful ring adorned with a brilliant aquamarine.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Ring of Magic](tech-ring_of_magic.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Aquamarine](item-gem_aquamarine.md) | 1 |
| [Empty Setting](item-gem_setting.md) | 1 |
| [Elegant Ring](item-simple_ring.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Ring of Magic](item-ring_of_magic.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_aquamarine\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_setting\", 1),\n\t\t\t\tnew CraftingReagent(\"simple_ring\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"ring_of_magic\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:79`
- `Assets.Source.Items/CraftingRecipe.cs:1`
