# Biological Experimentation recipe

In search of new breakthroughs in biological studies.

## In the game

In search of new breakthroughs in biological studies.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 2.5 seconds |
| Research | [Biological Experimentation](tech-biological_experiment.md) |
| Currency reward per batch | 16 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Doodad](item-doodad.md) | 1 |
| [Stalker Eye](item-stalker_eye.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "IconName": "\"Icons3_68\"",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"doodad\", 1),\n\t\t\t\tnew CraftingReagent(\"stalker_eye\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[0]",
  "CraftingReward": "new CurrencyCollection(Currency.Ingenuity, 16L)"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:87`
- `Assets.Source.Items/CraftingRecipe.cs:1`
