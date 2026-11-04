# Gremlin

A tiny but ferocious demon that can be used to help train your adventurers and fight your wars.

## In the game

A tiny but ferocious demon that can be used to help train your adventurers and fight your wars.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | gremlin |
| Item type | Combatant |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 120 |
| Armor | 35 |
| Combat Power | 210 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Summon Gremlin](recipe-summon_gremlin.md) | [Summoning Circle](building-SummoningCircle.md) | 12.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Demonic Initiation](recipe-cr_demonologist.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_217\"",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t120\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t35\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t210\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:298`
