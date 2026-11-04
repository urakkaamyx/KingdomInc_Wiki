# Flax Cultivation

Allows your farm to produce Flax.

## Research effect

Allows your farm to produce Flax.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_flax |
| Type | Resource |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |

## Leads to

| Research |
| --- |
| [Linen Cloth](tech-linen_cloth.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"farm\"",
  "IconName": "\"Icons2_26\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.FarmSettings.UnlockItem(ItemType.Get(\"flax\") as FarmItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:60`
- `Assets.Source.Player/TechNode.cs:1`
