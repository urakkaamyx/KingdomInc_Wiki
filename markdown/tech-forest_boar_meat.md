# Boar Hunt

Teaches your Hunters how to track and kill wild boars without being gored.

## Research effect

Teaches your Hunters how to track and kill wild boars without being gored.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_boar_meat |
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
  "IconName": "\"Icons_81\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"boar_meat\") as ForestItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:90`
- `Assets.Source.Player/TechNode.cs:1`
