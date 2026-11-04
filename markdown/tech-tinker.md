# Tinker

Experiment with a variety of base components to create all-new inventions and generate Ingenuity.

## Research effect

Experiment with a variety of base components to create all-new inventions and generate Ingenuity.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tinker |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |

## Related recipe

| Recipe |
| --- |
| [Tinker](recipe-tinker.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"inventor\"",
  "IconName": "\"Icons2_94\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:30`
- `Assets.Source.Player/TechNode.cs:1`
