# Relic of the Martyr

The bones of a fallen hero, carefully preserved in a gilded wooden locket. Bestows divine protection upon the bearer.

## Research effect

The bones of a fallen hero, carefully preserved in a gilded wooden locket. Bestows divine protection upon the bearer.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | martyr_relic |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |
| [Graveyard](tech-graveyard.md) |

## Related item

| Item |
| --- |
| [Relic of the Martyr](item-martyr_relic.md) |

## Related recipe

| Recipe |
| --- |
| [Relic of the Martyr](recipe-martyr_relic.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_78\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"graveyard\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:83`
- `Assets.Source.Player/TechNode.cs:1`
