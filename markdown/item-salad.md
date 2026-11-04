# Simple Salad

Make sure to always eat your vegetables.

## In the game

Make sure to always eat your vegetables.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | salad |
| Item type | Equipment |
| Slot | Food |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 30 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Simple Salad](recipe-salad.md) | [Campfire](building-Campfire.md) | 5.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_83\"",
  "Slot": "EquipmentSlot.Food",
  "BaseStats": "new StatSet { (stat: EquipStat.Magic, amt: 30) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier4.cs:57`
