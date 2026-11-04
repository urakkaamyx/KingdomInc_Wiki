# Guardian's Pledge

A sacred ritual to train a guardian into a Paladin.

## Research effect

A sacred ritual to train a guardian into a Paladin.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cr_paladin |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related recipe

| Recipe |
| --- |
| [Guardian's Pledge](recipe-cr_paladin.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons2_112\"",
  "CostCurrency": "CurrencyCollection.GoldFaith"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:91`
- `Assets.Source.Player/TechNode.cs:1`
