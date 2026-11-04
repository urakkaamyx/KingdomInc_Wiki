# Embroider Clothing: Defense recipe

Embroider a piece of light or medium armor to provide additional Armor.

## In the game

Embroider a piece of light or medium armor to provide additional Armor.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Engraver](building-Engraver.md) |
| Base crafting time | 3.5 seconds |
| Research | [Embroider Clothing: Defense](tech-engrave_light_armor_armor.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| Clothing (any type) | 1 |
| [Silver Thread](item-silver_thread.md) | 2 |
| [Bone](item-bone.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Embroider Clothing: Defense](enhancement-engrave_light_armor_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_101\"",
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tcraftingReagent2,\n\t\t\t\tnew CraftingReagent(\"silver_thread\", 2),\n\t\t\t\tnew CraftingReagent(\"bone\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"engrave_light_armor_armor\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Engraver.cs:81`
- `Assets.Source.Items/CraftingRecipe.cs:1`
