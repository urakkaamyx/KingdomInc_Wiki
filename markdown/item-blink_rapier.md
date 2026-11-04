# Ethereal Rapier

The thin blade of this sword is only connected to the hilt in some unseen dimension, allowing the point to bypass armor with ease.

## In the game

The thin blade of this sword is only connected to the hilt in some unseen dimension, allowing the point to bypass armor with ease.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | blink_rapier |
| Item type | Weapon |
| Weapon Type | Rapier |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 280 |
| Health | 90 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ethereal Rapier](recipe-blink_rapier.md) | [Shrine](building-Shrine.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_22\"",
  "WeaponType": "WeaponType.Rapier",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 280),\n\t\t\t\t(stat: EquipStat.Health, amt: 90)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:289`
