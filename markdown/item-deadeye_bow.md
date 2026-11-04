# Deadeye Bow

Demonic flesh bursts forth and covers the shooter's hand, correcting their aim and infecting their arrows with hellish rot.

## In the game

Demonic flesh bursts forth and covers the shooter's hand, correcting their aim and infecting their arrows with hellish rot.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | deadeye_bow |
| Item type | Weapon |
| Weapon Type | Bow |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 400 |
| Health | 140 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Deadeye Bow](recipe-deadeye_bow.md) | [Shrine](building-Shrine.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_26\"",
  "WeaponType": "WeaponType.Bow",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 400),\n\t\t\t\t(stat: EquipStat.Health, amt: 140)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:319`
