# Hellspawn

A hulking demoning creature dredged up from the depths of the underworld.

## In the game

A hulking demoning creature dredged up from the depths of the underworld.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | hellspawn |
| Item type | Combatant |
| Weapon Type Override | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 230 |
| Armor | 55 |
| Combat Power | 510 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Summon Hellspawn](recipe-summon_hellspawn.md) | [Summoning Circle](building-SummoningCircle.md) | 16.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_64\"",
  "WeaponTypeOverride": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t230\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t55\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t510\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:317`
