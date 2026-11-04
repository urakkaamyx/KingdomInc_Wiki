# Harvest Wild Onion

Teaches your Foragers how to identify and harvest wild Onions.

## Research effect

Teaches your Foragers how to identify and harvest wild Onions.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_wild_onion |
| Type | Resource |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |
| [Kitchen](tech-kitchen.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"forest\"",
  "IconName": "\"Icons2_180\"",
  "CostTier": "7",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"wild_onion\") as ForestItemType);\n\t\t\t}",
  "AdditionalRequirements": "new List<string> { \"kitchen\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:160`
- `Assets.Source.Player/TechNode.cs:1`
