# Cattle Husbandry

Allows your Farm to produce Cattle.

## Research effect

Allows your Farm to produce Cattle.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_cattle |
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
  "IconName": "\"Icons_190\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.FarmSettings.UnlockItem(ItemType.Get(\"cattle\") as FarmItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:40`
- `Assets.Source.Player/TechNode.cs:1`
