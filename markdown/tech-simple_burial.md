# Simple Burial

A clean, no-frills way to lay your dead to rest.

## Research effect

A clean, no-frills way to lay your dead to rest.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | simple_burial |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |

## Related recipe

| Recipe |
| --- |
| [Simple Burial](recipe-simple_burial.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"graveyard\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "IconName": "\"Icons2_82\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Graveyard.cs:36`
- `Assets.Source.Player/TechNode.cs:1`
