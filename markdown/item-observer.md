# Watcher

An ominous floating creature that attacks enemies from afar using its chaotic eyebeams.

## In the game

An ominous floating creature that attacks enemies from afar using its chaotic eyebeams.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | observer |
| Item type | Combatant |
| Weapon Type Override | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 560 |
| Armor | 65 |
| Combat Power | 730 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Summon Watcher](recipe-summon_observer.md) | [Summoning Circle](building-SummoningCircle.md) | 16.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_162\"",
  "WeaponTypeOverride": "WeaponType.Staff",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t560\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t65\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t730\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:343`
