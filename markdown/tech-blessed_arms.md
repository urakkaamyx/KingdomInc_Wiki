# Blessed Armaments

Extends a holy blessing over any weapon, increasing its Quality.

## Research effect

Extends a holy blessing over any weapon, increasing its Quality.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blessed_arms |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related recipe

| Recipe |
| --- |
| [Blessed Armaments](recipe-blessed_arms.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_75\"",
  "CostCurrency": "CurrencyCollection.GoldFaith"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:62`
- `Assets.Source.Player/TechNode.cs:1`
