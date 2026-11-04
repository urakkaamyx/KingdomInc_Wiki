# Bulwark of Ancients

An impenetrable shield to protect the innocent and smite the villainous.

## In the game

An impenetrable shield to protect the innocent and smite the villainous.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ancient_shield |
| Item type | Weapon |
| Weapon Type | Shield |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 120 |
| Health | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Bulwark of Ancients](recipe-ancient_shield.md) | [Carpenter](building-Carpenter.md) | 4.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_25\"",
  "WeaponType": "WeaponType.Shield",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 120),\n\t\t\t\t(stat: EquipStat.Health, amt: 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:134`
