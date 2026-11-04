# Luxury Shop

Allows you to sell high-quality items at a premium rate. Also serves as a secondary source of Crowns.

## Research effect

Allows you to sell high-quality items at a premium rate. Also serves as a secondary source of Crowns.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | luxury_shop |
| Type | Flow Element |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Restaurant](tech-restaurant.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"restaurant\"",
  "RelativePosition": "new Vector2Int(0, -254)",
  "IconName": "\"Icons_189\"",
  "CostMultiplier": "5.0",
  "CostCurrency": "CurrencyCollection.GoldCrown"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:99`
- `Assets.Source.Player/TechNode.cs:1`
