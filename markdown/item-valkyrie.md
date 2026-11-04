# Valkyrie

A holy angelic warrior who smites her foes with divine fury.

## In the game

A holy angelic warrior who smites her foes with divine fury.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | valkyrie |
| Item type | Combatant |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 290 |
| Armor | 120 |
| Combat Power | 590 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Summon Valkyrie](recipe-summon_valkyrie.md) | [Summoning Circle](building-SummoningCircle.md) | 16.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_164\"",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t290\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t120\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t590\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:370`
