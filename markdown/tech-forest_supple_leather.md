# Stalker Hunt

Teaches your Hunters to track and dispatch the nimble stalkers that can be harvested for Supple Leather.

## Research effect

Teaches your Hunters to track and dispatch the nimble stalkers that can be harvested for Supple Leather.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_supple_leather |
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
| [Embossed Leather](tech-embossed_leather.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"forest\"",
  "IconName": "\"Icons2_18\"",
  "CostTier": "6",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"supple_leather\") as ForestItemType);\n\t\t\t}",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:148`
- `Assets.Source.Player/TechNode.cs:1`
