# Skeletal Archer

A skeletal minion, its tendons reinforced to be able to draw back the bow made out of its own ribs.

## In the game

A skeletal minion, its tendons reinforced to be able to draw back the bow made out of its own ribs.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | skeletal_archer |
| Item type | Combatant |
| Weapon Type Override | Bow |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 210 |
| Armor | 50 |
| Combat Power | 590 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Skeletal Archer](recipe-skeletal_archer.md) | [Necromancer](building-Necromancer.md) | 20.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_83\"",
  "WeaponTypeOverride": "WeaponType.Bow",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t210\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t50\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t590\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:70`
