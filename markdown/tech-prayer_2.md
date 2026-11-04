# Ritual Prayer

A more powerful prayer that would be more likely to garner Saint Ilonia's favor.

## Research effect

A more powerful prayer that would be more likely to garner Saint Ilonia's favor.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | prayer_2 |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related recipe

| Recipe |
| --- |
| [Ritual Prayer](recipe-prayer_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_73\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:46`
- `Assets.Source.Player/TechNode.cs:1`
