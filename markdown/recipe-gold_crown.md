# Sapphire Crown recipe

An ornate piece of jewelry, sometimes worn by the aristocracy in honor of the late King.

## In the game

An ornate piece of jewelry, sometimes worn by the aristocracy in honor of the late King.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 3 seconds |
| Research | [Sapphire Crown](tech-gold_crown.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 2 |
| [Sapphire](item-sapphire.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Sapphire Crown](item-gold_crown.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gold_ingot\", 2),\n\t\t\t\tnew CraftingReagent(\"sapphire\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"gold_crown\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:100`
- `Assets.Source.Items/CraftingRecipe.cs:1`
