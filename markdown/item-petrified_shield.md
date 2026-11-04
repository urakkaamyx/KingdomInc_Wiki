# Petrified Shield

An impenetrable bulwark safeguarding the wielder and their allies.

## In the game

An impenetrable bulwark safeguarding the wielder and their allies.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | petrified_shield |
| Item type | Weapon |
| Weapon Type | Shield |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 180 |
| Health | 90 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Petrified Shield](recipe-petrified_shield.md) | [Carpenter](building-Carpenter.md) | 4.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Possessed Shield](recipe-infected_shield.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_27\"",
  "WeaponType": "WeaponType.Shield",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 180),\n\t\t\t\t(stat: EquipStat.Health, amt: 90)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:131`
