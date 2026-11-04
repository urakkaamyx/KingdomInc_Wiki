# Prayer Beads recipe

An ornate necklace of blessed gold and silver beads, intended to be used in ritualized prayer.

## In the game

An ornate necklace of blessed gold and silver beads, intended to be used in ritualized prayer.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 4 seconds |
| Research | [Prayer Beads](tech-prayer_beads.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 2 |
| [Silver Ingot](item-silver_ingot.md) | 2 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Prayer Beads](item-prayer_beads.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 2),\n\t\t\t\tnew CraftingReagent(\"silver_ingot\", 2),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"prayer_beads\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:337`
- `Assets.Source.Items/CraftingRecipe.cs:1`
