# Unlife Staff

A mockery of the natural world. Demonic vines shoot out to entrap the wielder's foes, forcing them to bow in submission.

## In the game

A mockery of the natural world. Demonic vines shoot out to entrap the wielder's foes, forcing them to bow in submission.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | unlife_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 400 |
| Health | 140 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Unlife Staff](recipe-unlife_staff.md) | [Shrine](building-Shrine.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_32\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 400),\n\t\t\t\t(stat: EquipStat.Health, amt: 140)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:339`
