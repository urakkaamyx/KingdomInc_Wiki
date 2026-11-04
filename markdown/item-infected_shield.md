# Possessed Shield

The demonic creature trapped inside the shield threatens to curse anyone that dares to strike it.

## In the game

The demonic creature trapped inside the shield threatens to curse anyone that dares to strike it.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | infected_shield |
| Item type | Weapon |
| Weapon Type | Shield |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 240 |
| Health | 120 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Possessed Shield](recipe-infected_shield.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_28\"",
  "WeaponType": "WeaponType.Shield",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 240),\n\t\t\t\t(stat: EquipStat.Health, amt: 120)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:192`
