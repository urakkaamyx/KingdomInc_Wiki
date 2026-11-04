# Wolf Hunt

Teaches your Hunters to hunt ferocious wolves and supply Wolf Hide.

## Research effect

Teaches your Hunters to hunt ferocious wolves and supply Wolf Hide.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_wolf_hide |
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
  "IconName": "\"Icons_77\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"wolf_hide\") as ForestItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:60`
- `Assets.Source.Player/TechNode.cs:1`
