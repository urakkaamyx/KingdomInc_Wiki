# Prayer of Light

Memorizing the entire thousand-page prayer allows a priest to train as a Lightbringer.

## Research effect

Memorizing the entire thousand-page prayer allows a priest to train as a Lightbringer.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cr_lightbringer |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Related recipe

| Recipe |
| --- |
| [Prayer of Light](recipe-cr_lightbringer.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons2_142\"",
  "CostCurrency": "CurrencyCollection.GoldFaith"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:112`
- `Assets.Source.Player/TechNode.cs:1`
