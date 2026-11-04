# Harvest Bone

Teaches your Hunters to identify and extract powerful Bones.

## Research effect

Teaches your Hunters to identify and extract powerful Bones.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_bone |
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
| [Iron Rapier](tech-iron_rapier.md) |
| [Staff of the Wild](tech-wild_staff.md) |
| [Engrave Heavy Armor: Defense](tech-engrave_heavy_armor_armor.md) |
| [Embroider Clothing: Defense](tech-engrave_light_armor_armor.md) |
| [Engrave Weapon: Strength](tech-engrave_weapon_str.md) |
| [Mushroom Stew](tech-mushroom_stew.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"forest\"",
  "IconName": "\"Icons_128\"",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"forest\", 3)",
  "CustomRequirementDesc": "\"@forest_den_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"bone\") as ForestItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:112`
- `Assets.Source.Player/TechNode.cs:1`
