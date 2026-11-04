# Rough Leather Hat

The itchy leather and coarse stitching will make any wearer go mad over time.

## In the game

The itchy leather and coarse stitching will make any wearer go mad over time.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | rough_leather_hat |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Medium |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 25 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Rough Leather Hat](recipe-rough_leather_hat.md) | [Leatherworker](building-Leatherworker.md) | 2.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_46\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Medium",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 25) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:64`
