# Doodad

A wondrous biochemical concoction.

## Research effect

A wondrous biochemical concoction.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | doodad |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Doodad](item-doodad.md) |

## Related recipe

| Recipe |
| --- |
| [Doodad](recipe-doodad.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"inventor\"",
  "IconName": "\"Icons2_93\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity",
  "CostMultiplier": "0.5"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:54`
- `Assets.Source.Player/TechNode.cs:1`
