# Market Maker

Reduces Currency Exchange tax by 50%.

## Research effect

Reduces Currency Exchange tax by 50%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | currency_exchange_tax |
| Type | Utility |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Currency Exchange](tech-currency_exchange.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"currency_exchange\"",
  "RelativePosition": "new Vector2Int(-180, 0)",
  "CostMultiplier": "8.0",
  "IconName": "\"Icons_149\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:179`
- `Assets.Source.Player/TechNode.cs:1`
