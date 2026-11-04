# Wheat Cultivation

Allows your farm to produce Wheat.

## Research effect

Allows your farm to produce Wheat.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_wheat |
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
  "IconName": "\"Icons_191\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.FarmSettings.UnlockItem(ItemType.Get(\"wheat\") as FarmItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:50`
- `Assets.Source.Player/TechNode.cs:1`
