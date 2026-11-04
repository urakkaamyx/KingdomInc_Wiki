# Salamander Skewer

A delicious fiery treat.

## In the game

A delicious fiery treat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | salamander_skewer |
| Item type | Equipment |
| Slot | Food |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 50 |

## Traits

| Trait |
| --- |
| [Fire Resist](trait-FireResist.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Salamander Skewer](recipe-salamander_skewer.md) | [Kitchen](building-Kitchen.md) | 5.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_174\"",
  "Slot": "EquipmentSlot.Food",
  "BaseStats": "new StatSet { (stat: EquipStat.Health, amt: 50) }",
  "EquipTrait": "AdventurerTrait.FireResist"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:78`
