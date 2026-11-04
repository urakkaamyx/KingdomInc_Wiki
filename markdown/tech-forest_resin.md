# Harvest Resin

Teaches your Lumberjacks to extract Resin from pine trees.

## Research effect

Teaches your Lumberjacks to extract Resin from pine trees.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_resin |
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
| [Embroider Clothing: Dexterity](tech-engrave_light_armor_dex.md) |
| [Engrave Weapon: Dexterity](tech-engrave_weapon_dex.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"forest\"",
  "IconName": "\"Icons_127\"",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"forest\", 3)",
  "CustomRequirementDesc": "\"@forest_den_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"resin\") as ForestItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:100`
- `Assets.Source.Player/TechNode.cs:1`
