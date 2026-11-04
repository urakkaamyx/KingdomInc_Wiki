# Scholar's Robe

A robe worn by seasoned mages and clerics. The delicate symbols woven into the fabric enhance the wearer's magic.

## In the game

A robe worn by seasoned mages and clerics. The delicate symbols woven into the fabric enhance the wearer's magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | cotton_robe |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 40 |
| Magic | 40 |
| Wisdom | 40 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Scholar's Robe](recipe-cotton_robe.md) | [Tailor](building-Tailor.md) | 3.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_32\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 40),\n\t\t\t\t(stat: EquipStat.Magic, amt: 40),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:138`
