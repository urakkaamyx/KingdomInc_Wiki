# Skeletal Archmage

A cunning undead sorcerer capable of raining hellfire upon your enemies.

## In the game

A cunning undead sorcerer capable of raining hellfire upon your enemies.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | skeletal_mage |
| Item type | Combatant |
| Weapon Type Override | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 240 |
| Armor | 60 |
| Combat Power | 930 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Skeletal Archmage](recipe-skeletal_mage.md) | [Necromancer](building-Necromancer.md) | 20.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_85\"",
  "WeaponTypeOverride": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t240\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t60\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t930\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:109`
