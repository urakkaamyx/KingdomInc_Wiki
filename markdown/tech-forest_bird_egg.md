# Harvest Bird Eggs

Teaches your Foragers how to spot camouflaged nests and supply Small Bird Eggs.

## Research effect

Teaches your Foragers how to spot camouflaged nests and supply Small Bird Eggs.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_bird_egg |
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
  "IconName": "\"Icons_78\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings.UnlockItem(ItemType.Get(\"bird_egg\") as ForestItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:70`
- `Assets.Source.Player/TechNode.cs:1`
