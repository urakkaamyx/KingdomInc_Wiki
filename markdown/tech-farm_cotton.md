# Cotton Cultivation

Allows your farm to produce Cotton.

## Research effect

Allows your farm to produce Cotton.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_cotton |
| Type | Resource |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |

## Leads to

| Research |
| --- |
| [Cotton Cloth](tech-cotton_cloth.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"farm\"",
  "IconName": "\"Icons2_27\"",
  "CostMultiplier": "1.5",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.FarmSettings.UnlockItem(ItemType.Get(\"cotton\") as FarmItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:70`
- `Assets.Source.Player/TechNode.cs:1`
