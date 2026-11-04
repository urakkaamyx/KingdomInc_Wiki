# Linen Cloth

Coarse and crude, but provides protection from the elements.

## In the game

Coarse and crude, but provides protection from the elements.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | linen_cloth |
| Item type | Resource |
| Resource Value | 100 |
| Quota Amount | 0.5 |
| Quota Base Cost | ResourceItemType.DefaultResourceCost * 1.25 |
| Tag | Supply |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Supply Depot](building-SupplyDepot.md) | [Supply Linen Cloth](tech-supply_linen_cloth.md) | 0.5 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Linen Cloth](recipe-linen_cloth.md) | [Tailor](building-Tailor.md) | 1.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Linen Padding](recipe-linen_padding.md) | 1 |
| [Simple Robe](recipe-simple_robe.md) | 3 |
| [Initiate's Hat](recipe-initiate_hat.md) | 2 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_49\"",
  "ResourceValue": "100L",
  "QuotaAmount": "0.5",
  "QuotaBaseCost": "ResourceItemType.DefaultResourceCost * 1.25",
  "Tag": "ResourceTag.Supply"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:10`
