# Band of Tranquility

The ring constantly sheds tiny seeds that drift off on the wind and sprout alien flowers in the countryside.

## In the game

The ring constantly sheds tiny seeds that drift off on the wind and sprout alien flowers in the countryside.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ring_of_wisdom_2 |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Band of Tranquility](recipe-ring_of_wisdom_2.md) | [Jeweler](building-Jeweler.md) | 9.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Pontiff's Ring](recipe-pontiff_ring.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_209\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Wisdom, amt: 100) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:113`
