# Seared Boar Steak

The simplest way to grill a piece of meat: Just throw it in a fire.

## In the game

The simplest way to grill a piece of meat: Just throw it in a fire.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | boar_steak |
| Item type | Equipment |
| Slot | Food |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 25 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Seared Boar Steak](recipe-boar_steak.md) | [Campfire](building-Campfire.md) | 8.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Feeding the Wildlife](recipe-cr_beast_master.md) | 2 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_82\"",
  "Slot": "EquipmentSlot.Food",
  "BaseStats": "new StatSet { (stat: EquipStat.Strength, amt: 25) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier4.cs:45`
