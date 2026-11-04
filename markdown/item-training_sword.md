# Training Sword

A basic wooden sword. Not made for actual combat, but widely available and surprisingly sturdy.

## In the game

A basic wooden sword. Not made for actual combat, but widely available and surprisingly sturdy.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | training_sword |
| Item type | Weapon |
| Weapon Type | Sword |
| Resource Value | 560 |
| Resource Cost | new CurrencyCollection().Add(Currency.Ring, 2L) |
| Tag | Adventure Supplies |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 50 |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Adventure Supplies](building-AdventureSupplies.md) | [Training Sword](tech-training_sword.md) | 1.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_75\"",
  "WeaponType": "WeaponType.Sword",
  "ResourceValue": "560L",
  "ResourceCost": "new CurrencyCollection().Add(Currency.Ring, 2L)",
  "Tag": "ResourceTag.AdventureSupplies",
  "BaseStats": "new StatSet { (stat: EquipStat.Strength, amt: 50) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier5.cs:36`
