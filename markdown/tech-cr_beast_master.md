# Feeding the Wildlife

Getting in tune with nature allows a ranger to train as a Beast Master.

## Research effect

Getting in tune with nature allows a ranger to train as a Beast Master.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cr_beast_master |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Campfire](tech-campfire.md) |
| [Scribe](tech-scribe.md) |

## Related recipe

| Recipe |
| --- |
| [Feeding the Wildlife](recipe-cr_beast_master.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"campfire\"",
  "IconName": "\"Icons2_124\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"scribe\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Campfire.cs:47`
- `Assets.Source.Player/TechNode.cs:1`
