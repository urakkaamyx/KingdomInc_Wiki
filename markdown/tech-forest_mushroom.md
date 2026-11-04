# Harvest Mushrooms

Teaches your Foragers how to identify and collect edible Mushrooms.

## Research effect

Teaches your Foragers how to identify and collect edible Mushrooms.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_mushroom |
| Type | Resource |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |

## Additional condition

Requires war progress: Feral Den

## Campaign condition

forest:3 (campaign ID : completed stage)

## Leads to

| Research |
| --- |
| [Embroider Clothing: Magic](tech-engrave_light_armor_mag.md) |
| [Engrave Weapon: Magic](tech-engrave_weapon_mag.md) |
| [Mushroom Stew](tech-mushroom_stew.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"forest\"",
  "IconName": "\"Icons_126\"",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"forest\", 3)",
  "CustomRequirementDesc": "\"@forest_den_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"mushroom\") as ForestItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:124`
- `Assets.Source.Player/TechNode.cs:1`
