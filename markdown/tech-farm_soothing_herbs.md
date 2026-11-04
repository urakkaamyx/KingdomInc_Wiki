# Herb Cultivation

Allows your farm to produce Soothing Herbs.

## Research effect

Allows your farm to produce Soothing Herbs.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_soothing_herbs |
| Type | Resource |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |
| [Alchemist](tech-alchemist.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"farm\"",
  "IconName": "\"Icons_224\"",
  "CostMultiplier": "1.5",
  "AdditionalRequirements": "new List<string> { \"alchemist\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.FarmSettings.UnlockItem(ItemType.Get(\"soothing_herbs\") as FarmItemType);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:113`
- `Assets.Source.Player/TechNode.cs:1`
