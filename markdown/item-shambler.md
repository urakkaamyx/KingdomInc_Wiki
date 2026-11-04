# Undead Shambler

A simple undead creature that even a rookie necromancer could reanimate.

## In the game

A simple undead creature that even a rookie necromancer could reanimate.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | shambler |
| Item type | Combatant |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 270 |
| Armor | 45 |
| Combat Power | 380 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Undead Shambler](recipe-shambler.md) | [Necromancer](building-Necromancer.md) | 16.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_86\"",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t270\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t45\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t380\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:51`
