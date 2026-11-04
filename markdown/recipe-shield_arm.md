# Puppet Shield recipe

A clockwork arm that straps to the wearer's back, holding a small round shield. Its rudimentary mago-tech brain predicts and blocks incoming enemy attacks.

## In the game

A clockwork arm that straps to the wearer's back, holding a small round shield. Its rudimentary mago-tech brain predicts and blocks incoming enemy attacks.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Inventor](building-Inventor.md) |
| Base crafting time | 2.5 seconds |
| Research | [Puppet Shield](tech-shield_arm.md) |
| Currency consumed per batch | 60 Ingenuity |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 1 |
| [Petrified Wood](item-petrified_wood.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Puppet Shield](item-shield_arm.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingCost": "new CurrencyCollection(Currency.Ingenuity, 60L)",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 1),\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"shield_arm\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:223`
- `Assets.Source.Items/CraftingRecipe.cs:1`
