# Apothecary's Tome

Contains a variety of medicinal recipes and practical tips for the aspiring doctor. Medical education not required.

## Research effect

Contains a variety of medicinal recipes and practical tips for the aspiring doctor. Medical education not required.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tome_of_health |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |

## Related item

| Item |
| --- |
| [Apothecary's Tome](item-tome_of_health.md) |

## Related recipe

| Recipe |
| --- |
| [Apothecary's Tome](recipe-tome_of_health.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_64\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:76`
- `Assets.Source.Player/TechNode.cs:1`
