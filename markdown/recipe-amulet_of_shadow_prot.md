# Amulet of Dark Tidings recipe

Projects an aura of death and hopelessness in an attempt to protect the wearer and their allies from dark magic.

## In the game

Projects an aura of death and hopelessness in an attempt to protect the wearer and their allies from dark magic.

## Crafting

Base time excludes worker speed, productivity, input starvation, output blocking and quotas. A result that names an enhancement modifies the selected item rather than creating a new loose item.

| Property | Value |
| --- | --- |
| Station | [Jeweler](building-Jeweler.md) |
| Base crafting time | 3 seconds |
| Research | [Amulet of Dark Tidings](tech-amulet_of_shadow_prot.md) |

## Ingredients

| Item or selection | Count / rule |
| --- | --- |
| [Diamond Chip](item-gem_diamond.md) | 1 |
| [Empty Setting](item-gem_setting.md) | 1 |
| [Supple String](item-supple_string.md) | 1 |

## Results

| Item or selection | Count / rule |
| --- | --- |
| [Amulet of Dark Tidings](item-amulet_of_shadow_prot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "Tag": "tag",
  "Reagents": "new CraftingReagent[3]\n\t\t\t{\n\t\t\t\tnew CraftingReagent(\"gem_diamond\", 1),\n\t\t\t\tnew CraftingReagent(\"gem_setting\", 1),\n\t\t\t\tnew CraftingReagent(\"supple_string\", 1)\n\t\t\t}",
  "Results": "new CraftingResult[1]\n\t\t\t{\n\t\t\t\tnew CraftingResult(\"amulet_of_shadow_prot\", 1)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Recipes/Jeweler.cs:267`
- `Assets.Source.Items/CraftingRecipe.cs:1`
