# Harvest Wood Log

Teaches your Lumberjacks to cut down trees and supply Wood Logs.

## Research effect

Teaches your Lumberjacks to cut down trees and supply Wood Logs.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_wood_log |
| Type | Resource |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"forest\"",
  "IconName": "\"Icons_13\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"wood_log\") as ForestItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:50`
- `Assets.Source.Player/TechNode.cs:1`
