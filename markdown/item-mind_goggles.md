# Leyline Goggles

Allows the wearer to detect and identify subtle magical influences embedded in the environment.

## In the game

Allows the wearer to detect and identify subtle magical influences embedded in the environment.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | mind_goggles |
| Item type | Equipment |
| Slot | Trinket |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 20 |

## Traits

| Trait |
| --- |
| [Magic Skill Crit](trait-MagicSkillCrit.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Leyline Goggles](recipe-mind_goggles.md) | [Inventor](building-Inventor.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_52\"",
  "Slot": "EquipmentSlot.Trinket",
  "BaseStats": "new StatSet { (stat: EquipStat.Magic, amt: 20) }",
  "EquipTrait": "AdventurerTrait.MagicSkillCrit"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:234`
