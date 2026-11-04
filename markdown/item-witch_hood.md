# Witch Hood

The living cloth whispers impossible promises and mad prophecies to the wearer.

## In the game

The living cloth whispers impossible promises and mad prophecies to the wearer.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | witch_hood |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 30 |
| Magic | 60 |
| Wisdom | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Witch Hood](recipe-witch_hood.md) | [Tailor](building-Tailor.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Archmage's Hat](recipe-archmage_hat.md) | 1 |
| [Dark Prophet's Hood](recipe-prophet_hood.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_9\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 30),\n\t\t\t\t(stat: EquipStat.Magic, amt: 60),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:154`
