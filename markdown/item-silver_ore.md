# Silver Ore

Small flecks of pure silver are visible in the rock's dull surface.

## In the game

Small flecks of pure silver are visible in the rock's dull surface.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | silver_ore |
| Item type | Resource |
| Resource Value | 250 |
| Resource Cost | new CurrencyCollection().Add(Currency.Gold, 75L) |
| Quota Amount | 0.5 |
| Quota Base Cost | new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 1.25).Add(Currency.Medal, 10L) |
| Tag | Mine |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Mine](building-Mine.md) | [Mine Silver Ore](tech-mine_silver_ore.md) | 0.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Silver Ingot](recipe-silver_ingot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_87\"",
  "ResourceValue": "250L",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Gold, 75L)",
  "QuotaAmount": "0.5",
  "QuotaBaseCost": "new CurrencyCollection().Add(ResourceItemType.DefaultResourceCost * 1.25).Add(Currency.Medal, 10L)",
  "Tag": "ResourceTag.Mine"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier3.cs:92`
