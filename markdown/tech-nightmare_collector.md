# Nightmare Collector

The pinnacle of mago-tech engineering, designed to extract the living energy of a dreaming God.

## Research effect

The pinnacle of mago-tech engineering, designed to extract the living energy of a dreaming God.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | nightmare_collector |
| Type | Recipe |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |
| [Nightmare Distiller](tech-nightmare_distiller.md) |

## Related item

| Item |
| --- |
| [Nightmare Collector](item-nightmare_collector.md) |

## Related recipe

| Recipe |
| --- |
| [Nightmare Collector](recipe-nightmare_collector.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"inventor\"",
  "IconName": "\"Icons3_91\"",
  "AdditionalRequirements": "new List<string> { \"nightmare_distiller\" }",
  "CostTier": "12",
  "CostCurrency": "CurrencyCollection.GoldIngenuity"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:163`
- `Assets.Source.Player/TechNode.cs:1`
