# Tinkersteel Sword recipe

The sword will sometimes abruptly change direction in combat to strike from an unexpected angle.

## In the game

The sword will sometimes abruptly change direction in combat to strike from an unexpected angle.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Blacksmith](building-Blacksmith.md) |
| Base crafting time | 7 seconds |
| Research | [Tinkersteel Sword](tech-tinkersteel_sword.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel](item-tinkersteel.md) | 3 |
| [Petrified Wood](item-petrified_wood.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Tinkersteel Sword](item-tinkersteel_sword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "CraftingTimeMultiplier": "2f",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"tinkersteel\", 3),\n\t\t\t\tnew CraftingReagent(\"petrified_wood\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"tinkersteel_sword\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Blacksmith.cs:257`
- `Assets.Source.Items/CraftingRecipe.cs:1`
