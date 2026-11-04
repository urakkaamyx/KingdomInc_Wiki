# Archbishop's Staff

An honorable weapon of the high clergy. Its overwhelming presence demands both reverence and obedience.

## In the game

An honorable weapon of the high clergy. Its overwhelming presence demands both reverence and obedience.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | archbishop_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 300 |
| Health | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Archbishop's Staff](recipe-archbishop_staff.md) | [Carpenter](building-Carpenter.md) | 4.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Unlife Staff](recipe-unlife_staff.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_31\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 300),\n\t\t\t\t(stat: EquipStat.Health, amt: 100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:198`
