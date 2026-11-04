# Reconstructed Nightmare

A reconstituted essence of pure darkness.

## Research effect

A reconstituted essence of pure darkness.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | reconstructed_nightmare |
| Type | Recipe |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Nightmare Distiller](tech-nightmare_distiller.md) |

## Related item

| Item |
| --- |
| [Reconstructed Nightmare](item-reconstructed_nightmare.md) |

## Related recipe

| Recipe |
| --- |
| [Reconstructed Nightmare](recipe-reconstructed_nightmare.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "IconName": "\"Icons3_87\"",
  "AdditionalRequirements": "new List<string> { \"nightmare_distiller\" }",
  "CostTier": "12",
  "CostCurrency": "CurrencyCollection.GoldMana"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:142`
- `Assets.Source.Player/TechNode.cs:1`
