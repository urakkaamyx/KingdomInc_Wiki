# Currency Exchange

Allows you to exchange one currency for another, for a price.

Click a currency in the top bar to start a transaction.

## Research effect

Allows you to exchange one currency for another, for a price.

Click a currency in the top bar to start a transaction.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | currency_exchange |
| Type | Utility |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |

## Leads to

| Research |
| --- |
| [Market Maker](tech-currency_exchange_tax.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"inventor\"",
  "RelativePosition": "new Vector2Int(-405, 45)",
  "IconName": "\"Icons_119\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:172`
- `Assets.Source.Player/TechNode.cs:1`
