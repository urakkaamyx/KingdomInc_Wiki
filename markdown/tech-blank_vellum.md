# Blank Vellum

A traditional writing surface made from the skin of certain animals. Its inherent magical qualities make it very useful for writing prepared spells and arcane treatises.

## Research effect

A traditional writing surface made from the skin of certain animals. Its inherent magical qualities make it very useful for writing prepared spells and arcane treatises.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blank_vellum |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |

## Related item

| Item |
| --- |
| [Blank Vellum](item-blank_vellum.md) |

## Related recipe

| Recipe |
| --- |
| [Blank Vellum](recipe-blank_vellum.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"scribe\"",
  "IconName": "\"Icons3_36\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:24`
- `Assets.Source.Player/TechNode.cs:1`
