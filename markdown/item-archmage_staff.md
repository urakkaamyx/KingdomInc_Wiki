# Archmage's Staff

A high-ranking mage's beacon of authority, as well as the main source of their power.

## In the game

A high-ranking mage's beacon of authority, as well as the main source of their power.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | archmage_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 300 |
| Wisdom | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Archmage's Staff](recipe-archmage_staff.md) | [Carpenter](building-Carpenter.md) | 4.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Splintered Staff](recipe-fragment_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_29\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Magic, amt: 300),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:188`
