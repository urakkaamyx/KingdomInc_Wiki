# Decoded Writings recipe

After many attempts, the infernal runes have been translated into a form that mortal humans can comprehend.

## In the game

After many attempts, the infernal runes have been translated into a form that mortal humans can comprehend.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 9 seconds |
| Research | [Decoded Writings](tech-decoded_writings.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Blank Vellum](item-blank_vellum.md) | 1 |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |
| [Demonic Writings](item-demonic_writings.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Decoded Writings](item-decoded_writings.md) | 1 item at 10% probability |
| [Demonic Writings](item-demonic_writings.md) | 1 item at 90% probability |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons3_37\"",
  "CraftingTimeMultiplier": "3f",
  "BaseProductivity": "-999f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"blank_vellum\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_ink\", 1),\n\t\t\t\tnew CraftingReagent(\"demonic_writings\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[2]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"decoded_writings\", 0.1f),\n\t\t\t\tnew CraftingResult(\"demonic_writings\", 0.9f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:201`
- `Assets.Source.Items/CraftingRecipe.cs:1`
