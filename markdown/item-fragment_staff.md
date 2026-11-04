# Splintered Staff

Unable to contain its frightening power, the staff fractured into shards that are still bound together by some unseen force.

## In the game

Unable to contain its frightening power, the staff fractured into shards that are still bound together by some unseen force.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | fragment_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 400 |
| Health | 140 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Splintered Staff](recipe-fragment_staff.md) | [Shrine](building-Shrine.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_30\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Magic, amt: 400),\n\t\t\t\t(stat: EquipStat.Health, amt: 140)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:329`
