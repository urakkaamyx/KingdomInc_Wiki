# Ring of Magic

A powerful ring adorned with a brilliant aquamarine.

## In the game

A powerful ring adorned with a brilliant aquamarine.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ring_of_magic |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ring of Magic](recipe-ring_of_magic.md) | [Jeweler](building-Jeweler.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Monsoon Band](recipe-ring_of_magic_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_202\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Magic, amt: 50) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:71`
