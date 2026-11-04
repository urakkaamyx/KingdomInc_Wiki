# Mad Scribblings recipe

In a flash of deranged genius, one of your Mages can sketch out the designs for a novel mago-tech contraption.

## In the game

In a flash of deranged genius, one of your Mages can sketch out the designs for a novel mago-tech contraption.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Scribe](building-Scribe.md) |
| Base crafting time | 18 seconds |
| Research | [Mad Scribblings](tech-mad_scribblings.md) |
| Base productivity modifier | -999f |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Mage | 1 |
| [Blank Vellum](item-blank_vellum.md) | 1 |
| [Enchanted Ink](item-enchanted_ink.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| Custom selection | OutputMage(0.12f) |
| Custom selection | OutputIngenuity(74f) |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons3_95\"",
  "BaseProductivity": "-999f",
  "CraftingTimeMultiplier": "6f",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent((InventoryItem i) => i.Type is HumanItemType humanItemType && humanItemType.Archetype == AdventurerArchetype.Mage, 1, \"mage\", \"@mage\"),\n\t\t\t\tnew CraftingReagent(\"blank_vellum\", 1),\n\t\t\t\tnew CraftingReagent(\"enchanted_ink\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[2]\n\t\t\t{\n\t\t\t\tOutputMage(0.12f),\n\t\t\t\tOutputIngenuity(74f)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:43`
- `Assets.Source.Items/CraftingRecipe.cs:1`
