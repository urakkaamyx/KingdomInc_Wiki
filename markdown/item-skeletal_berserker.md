# Skeletal Berserker

With a skeletal structure reinforced by magical metal, this warrior fearlessly rushes into battle.

## In the game

With a skeletal structure reinforced by magical metal, this warrior fearlessly rushes into battle.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | skeletal_berserker |
| Item type | Combatant |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 220 |
| Armor | 120 |
| Combat Power | 630 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Skeletal Berserker](recipe-skeletal_berserker.md) | [Necromancer](building-Necromancer.md) | 20.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_84\"",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t220\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t120\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t630\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:90`
