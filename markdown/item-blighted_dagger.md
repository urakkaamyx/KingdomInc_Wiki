# Blighted Dagger

A system of hollow tubes constantly delivers a deadly mixture of flesh-devouring toxins to the tip of the blade.

## In the game

A system of hollow tubes constantly delivers a deadly mixture of flesh-devouring toxins to the tip of the blade.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | blighted_dagger |
| Item type | Weapon |
| Weapon Type | Dagger |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 240 |
| Health | 90 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Blighted Dagger](recipe-blighted_dagger.md) | [Shrine](building-Shrine.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_18\"",
  "WeaponType": "WeaponType.Dagger",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 240),\n\t\t\t\t(stat: EquipStat.Health, amt: 90)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:279`
