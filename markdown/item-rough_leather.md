# Rough Leather

Processed skin of a dead animal with surprisingly many use cases.

## In the game

Processed skin of a dead animal with surprisingly many use cases.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | rough_leather |
| Item type | Resource |
| Resource Value | 100 |
| Quota Amount | 0.5 |
| Quota Base Cost | ResourceItemType.DefaultResourceCost * 1.25 |
| Tag | Supply |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Supply Depot](building-SupplyDepot.md) | [Supply Rough Leather](tech-supply_rough_leather.md) | 0.5 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Butcher Cattle](recipe-butcher_cattle.md) | [Butcher](building-Butcher.md) | 6.0 |
| [Rough Leather](recipe-rough_leather.md) | [Leatherworker](building-Leatherworker.md) | 2.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Rough String](recipe-rough_string.md) | 1 |
| [Rough Vest](recipe-rough_vest.md) | 3 |
| [Rough Leather Hat](recipe-rough_leather_hat.md) | 2 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_45\"",
  "ResourceValue": "100L",
  "QuotaAmount": "0.5",
  "QuotaBaseCost": "ResourceItemType.DefaultResourceCost * 1.25",
  "Tag": "ResourceTag.Supply"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:18`
