# Crystalline Staff

A solid wood staff adorned with fragmented mana crystals and delicate gold detailing.

## In the game

A solid wood staff adorned with fragmented mana crystals and delicate gold detailing.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ancient_int_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 200 |
| Wisdom | 70 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Crystalline Staff](recipe-ancient_int_staff.md) | [Carpenter](building-Carpenter.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_22\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Magic, amt: 200),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 70)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:102`
