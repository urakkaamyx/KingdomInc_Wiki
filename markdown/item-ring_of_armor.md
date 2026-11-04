# Ring of Protection

A fortified ring adorned with three small sapphires.

## In the game

A fortified ring adorned with three small sapphires.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ring_of_armor |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 45 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ring of Protection](recipe-ring_of_armor.md) | [Jeweler](building-Jeweler.md) | 4.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Leaden Band](recipe-ring_of_armor_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_205\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 45) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:89`
