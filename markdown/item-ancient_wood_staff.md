# Ancient Wood Staff

Tough and unyielding, but its delicate carved patterns suggest a hidden purpose beyond raw strength.

## In the game

Tough and unyielding, but its delicate carved patterns suggest a hidden purpose beyond raw strength.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ancient_wood_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 200 |
| Magic | 70 |
| Wisdom | 70 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ancient Wood Staff](recipe-ancient_wood_staff.md) | [Carpenter](building-Carpenter.md) | 4.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Crystalline Staff](recipe-ancient_int_staff.md) | 1 |
| [Staff of Sages](recipe-ancient_wis_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_21\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 200),\n\t\t\t\t(stat: EquipStat.Magic, amt: 70),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 70)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:113`
