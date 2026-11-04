# Ring of Dexterity

An elegant ring adorned with a shifting emerald.

## In the game

An elegant ring adorned with a shifting emerald.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ring_of_dexterity |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ring of Dexterity](recipe-ring_of_dexterity.md) | [Jeweler](building-Jeweler.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Serpentine Band](recipe-ring_of_dexterity_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_201\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Dexterity, amt: 50) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:65`
