# Indulgence

A document issued by the divine bureaucracy that promises to erase the bearer's sins upon death.

## Research effect

A document issued by the divine bureaucracy that promises to erase the bearer's sins upon death.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | indulgence |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related item

| Item |
| --- |
| [Indulgence](item-indulgence.md) |

## Related recipe

| Recipe |
| --- |
| [Indulgence](recipe-indulgence.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_74\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:54`
- `Assets.Source.Player/TechNode.cs:1`
