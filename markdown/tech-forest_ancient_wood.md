# Harvest Ancient Wood

Teaches your Lumberjacks to identify and dismember the largest trees in the forest for Ancient Wood Logs.

## Research effect

Teaches your Lumberjacks to identify and dismember the largest trees in the forest for Ancient Wood Logs.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_ancient_wood |
| Type | Resource |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |
| [Enchanter](tech-enchanter.md) |

## Leads to

| Research |
| --- |
| [Ancient Wood Plank](tech-ancient_wood_plank.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"forest\"",
  "IconName": "\"Icons2_10\"",
  "CostTier": "6",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"ancient_wood_log\") as ForestItemType);\n\t\t\t}",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:136`
- `Assets.Source.Player/TechNode.cs:1`
