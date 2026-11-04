# Staff of Sages

A runecarved staff of ancient design, carried by sages and soothsayers for generations.

## In the game

A runecarved staff of ancient design, carried by sages and soothsayers for generations.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ancient_wis_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 200 |
| Health | 70 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Staff of Sages](recipe-ancient_wis_staff.md) | [Carpenter](building-Carpenter.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_23\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 200),\n\t\t\t\t(stat: EquipStat.Health, amt: 70)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:112`
