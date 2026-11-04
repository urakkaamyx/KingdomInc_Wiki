# Salamander Husbandry

Allows your farm to produce Salamanders.

## Research effect

Allows your farm to produce Salamanders.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_salamander |
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
  "IconName": "\"Icons2_172\"",
  "CostMultiplier": "1.5",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.FarmSettings.UnlockItem(ItemType.Get(\"salamander\") as FarmItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:81`
- `Assets.Source.Player/TechNode.cs:1`
