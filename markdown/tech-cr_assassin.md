# Anatomy Lesson

Learning from the masters of precision allows a thief to train as an Assassin.

## Research effect

Learning from the masters of precision allows a thief to train as an Assassin.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | cr_assassin |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Butcher](tech-butcher.md) |
| [Scribe](tech-scribe.md) |

## Related recipe

| Recipe |
| --- |
| [Anatomy Lesson](recipe-cr_assassin.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"butcher\"",
  "IconName": "\"Icons2_120\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"scribe\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Butcher.cs:46`
- `Assets.Source.Player/TechNode.cs:1`
