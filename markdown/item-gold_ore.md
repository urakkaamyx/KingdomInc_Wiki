# Gold Ore

Unrefined rocks from deep within the planet, containing a small amount of gold.

## In the game

Unrefined rocks from deep within the planet, containing a small amount of gold.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | gold_ore |
| Item type | Resource |
| Resource Value | 300 |
| Resource Cost | new CurrencyCollection().Add(Currency.Gold, 100L) |
| Quota Amount | 0.5 |
| Quota Base Cost | new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 1.5).Add(Currency.Medal, 15L) |
| Tag | Mine |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Mine](building-Mine.md) | [Mine Gold Ore](tech-mine_gold_ore.md) | 0.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Gold Ingot](recipe-gold_ingot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_88\"",
  "ResourceValue": "300L",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Gold, 100L)",
  "QuotaAmount": "0.5",
  "QuotaBaseCost": "new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 1.5).Add(Currency.Medal, 15L)",
  "Tag": "ResourceTag.Mine"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier3.cs:83`
