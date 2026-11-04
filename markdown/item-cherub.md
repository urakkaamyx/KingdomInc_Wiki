# Cherub

A small angelic creature empowered with healing magic.

## In the game

A small angelic creature empowered with healing magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | cherub |
| Item type | Combatant |
| Weapon Type Override | Bow |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 145 |
| Armor | 65 |
| Combat Power | 380 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Summon Cherub](recipe-summon_cherub.md) | [Summoning Circle](building-SummoningCircle.md) | 12.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_163\"",
  "WeaponTypeOverride": "WeaponType.Bow",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Health,\n\t\t\t\t\t145\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Armor,\n\t\t\t\t\t65\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t\t380\n\t\t\t\t}\n\t\t\t}",
  "ClassTraits": "new List<AdventurerTrait> { AdventurerTrait.MinorHealer }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:349`
