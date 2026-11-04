# Elegant Ring

A perfectly polished ring of alloyed gold and silver.

## In the game

A perfectly polished ring of alloyed gold and silver.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | simple_ring |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 20 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Elegant Ring](recipe-simple_ring.md) | [Jeweler](building-Jeweler.md) | 2.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Ring of Strength](recipe-ring_of_strength.md) | 1 |
| [Ring of Dexterity](recipe-ring_of_dexterity.md) | 1 |
| [Ring of Magic](recipe-ring_of_magic.md) | 1 |
| [Ring of Wisdom](recipe-ring_of_wisdom.md) | 1 |
| [Ring of Health](recipe-ring_of_health.md) | 1 |
| [Ring of Protection](recipe-ring_of_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_199\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Health, amt: 20) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:53`
