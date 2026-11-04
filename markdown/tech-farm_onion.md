# Onion Cultivation

Allows your farm to produce Onions.

## Research effect

Allows your farm to produce Onions.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_onion |
| Type | Resource |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"farm\"",
  "IconName": "\"Icons2_175\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.FarmSettings.UnlockItem(ItemType.Get(\"onion\") as FarmItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:92`
- `Assets.Source.Player/TechNode.cs:1`
