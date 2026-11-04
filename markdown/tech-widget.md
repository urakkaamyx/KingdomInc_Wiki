# Widget

A curious mechanical invention.

## Research effect

A curious mechanical invention.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | widget |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Widget](item-widget.md) |

## Related recipe

| Recipe |
| --- |
| [Widget](recipe-widget.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"inventor\"",
  "IconName": "\"Icons2_92\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:38`
- `Assets.Source.Player/TechNode.cs:1`
