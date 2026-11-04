# Scroll of Healing

The scroll's magic is consumed upon use to restore a large amount of health.

## Research effect

The scroll's magic is consumed upon use to restore a large amount of health.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | scroll_of_healing |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |

## Related item

| Item |
| --- |
| [Scroll of Healing](item-scroll_of_healing.md) |

## Related recipe

| Recipe |
| --- |
| [Scroll of Healing](recipe-scroll_of_healing.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_60\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:48`
- `Assets.Source.Player/TechNode.cs:1`
