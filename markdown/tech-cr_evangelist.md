# Preaching to the Choir

Powerful oration to the gathered followers allows a priest to train as an Evangelist.

## Research effect

Powerful oration to the gathered followers allows a priest to train as an Evangelist.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cr_evangelist |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related recipe

| Recipe |
| --- |
| [Preaching to the Choir](recipe-cr_evangelist.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons2_140\"",
  "CostCurrency": "CurrencyCollection.GoldFaith"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:105`
- `Assets.Source.Player/TechNode.cs:1`
