# Ring of Health

A pristine ring adorned with a robust ruby.

## In the game

A pristine ring adorned with a robust ruby.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ring_of_health |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ring of Health](recipe-ring_of_health.md) | [Jeweler](building-Jeweler.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Undying Band](recipe-ring_of_health_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_200\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Health, amt: 50) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:83`
