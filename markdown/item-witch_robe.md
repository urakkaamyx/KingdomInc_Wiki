# Witch Robe

An unworthy wearer will slowly have their soul siphoned away by the living fabric until nothing is left.

## In the game

An unworthy wearer will slowly have their soul siphoned away by the living fabric until nothing is left.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | witch_robe |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 50 |
| Magic | 60 |
| Wisdom | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Witch Robe](recipe-witch_robe.md) | [Tailor](building-Tailor.md) | 3.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Archmage's Robe](recipe-archmage_robe.md) | 1 |
| [Dark Prophet's Robe](recipe-prophet_robe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_11\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 50),\n\t\t\t\t(stat: EquipStat.Magic, amt: 60),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:142`
