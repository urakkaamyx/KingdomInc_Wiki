# Simple Robe

The robes provide no magical benefits, but an initiate wizard wouldn't want to be caught without one.

## In the game

The robes provide no magical benefits, but an initiate wizard wouldn't want to be caught without one.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | simple_robe |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 20 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Simple Robe](recipe-simple_robe.md) | [Tailor](building-Tailor.md) | 3.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_42\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 20) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:43`
