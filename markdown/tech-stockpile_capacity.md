# Dimensional Storage

Stockpile maximum capacity can be adjusted between 1 and 100 items.

## Research effect

Stockpile maximum capacity can be adjusted between 1 and 100 items.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | stockpile_capacity |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Stockpile](tech-stockpile.md) |
| [Enchanter](tech-enchanter.md) |

## Leads to

| Research |
| --- |
| [Overflowing Stockpile](tech-stockpile_overflow.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"stockpile\"",
  "RelativePosition": "new Vector2Int(45, 207)",
  "IconName": "\"Icons_199\"",
  "CostTier": "5",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:194`
- `Assets.Source.Player/TechNode.cs:1`
