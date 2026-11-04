# Engrave Heavy Armor: Health recipe

Engrave a piece of heavy armor to provide a minor Health bonus.

## In the game

Engrave a piece of heavy armor to provide a minor Health bonus.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3 seconds |
| Research | [Engrave Heavy Armor: Health](tech-engrave_heavy_armor_health.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Heavy Armor (any type) | 1 |
| [Gold Wire](item-gold_wire.md) | 2 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Engrave Heavy Armor: Health](enhancement-engrave_heavy_armor_health.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_92\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[2]\n\t\t\t{\n\t\t\t\tcraftingReagent,\n\t\t\t\tnew CraftingReagent(\"gold_wire\", 2)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_heavy_armor_health\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:38`
- `Assets.Source.Items/CraftingRecipe.cs:1`
