# Sapphire

An uncut blue gemstone, famed for both its beauty and its strong connection to magic.

## In the game

An uncut blue gemstone, famed for both its beauty and its strong connection to magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | sapphire |
| Item type | Resource |
| Resource Value | 400 |
| Resource Cost | new CurrencyCollection().Add(Currency.Gold, 160L) |
| Quota Amount | 0.2 |
| Quota Base Cost | new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 1.5).Add(Currency.Requisition, 8L) |
| Tag | Mine |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Mine](building-Mine.md) | [Mine Sapphire](tech-mine_sapphire.md) | 0.2 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Sapphire Crown](recipe-gold_crown.md) | 1 |
| [Initiate's Staff](recipe-initiate_staff.md) | 1 |
| [Ring of Protection](recipe-ring_of_armor.md) | 3 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_69\"",
  "ResourceValue": "400L",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Gold, 160L)",
  "QuotaAmount": "0.2",
  "QuotaBaseCost": "new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 1.5).Add(Currency.Requisition, 8L)",
  "Tag": "ResourceTag.Mine"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:26`
