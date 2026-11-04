# Pantry

A storage space for food and potions for a small fee. All pantries are linked and contents can be accessed from anywhere.

## Research effect

A storage space for food and potions for a small fee. All pantries are linked and contents can be accessed from anywhere.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | pantry |
| Type | Flow Element |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Restaurant](tech-restaurant.md) |

## Leads to

| Research |
| --- |
| [Deep Cavern Storage](tech-pantry_unlock_channels.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"restaurant\"",
  "RelativePosition": "new Vector2Int(0, 254)",
  "IconName": "\"Icons_187\"",
  "CostMultiplier": "2.0",
  "CostCurrency": "CurrencyCollection.GoldCrown"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:79`
- `Assets.Source.Player/TechNode.cs:1`
