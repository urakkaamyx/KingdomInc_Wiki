# Hulking Monstrosity

A fearsome undead monster, composed of several corpses stitched together into a single brute.

## In the game

A fearsome undead monster, composed of several corpses stitched together into a single brute.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | hulking_monstrosity |
| Item type | Combatant |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 675 |
| Armor | 100 |
| Combat Power | 810 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Hulking Monstrosity](recipe-hulking_monstrosity.md) | [Necromancer](building-Necromancer.md) | 28.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_88\"",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t675\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t100\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t810\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:129`
