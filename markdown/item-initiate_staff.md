# Initiate's Staff

Initiate wizards are given a staff during their training, adding their own magic over time.

## In the game

Initiate wizards are given a staff during their training, adding their own magic over time.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | initiate_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Initiate's Staff](recipe-initiate_staff.md) | [Carpenter](building-Carpenter.md) | 3.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_50\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet { (stat: EquipStat.Magic, amt: 100) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:77`
