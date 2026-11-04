# Harvest Lettuce

Teaches your Foragers how to identify and harvest wild Lettuce.

## Research effect

Teaches your Foragers how to identify and harvest wild Lettuce.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_lettuce |
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
  "IconName": "\"Icons_80\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"lettuce\") as ForestItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:80`
- `Assets.Source.Player/TechNode.cs:1`
