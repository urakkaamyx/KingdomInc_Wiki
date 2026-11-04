# Assassin's Goggles

Automatically highlights the target's weakspots for the wearer.

A character can only benefit from a single source of Critical Hit.

## In the game

Automatically highlights the target's weakspots for the wearer.

A character can only benefit from a single source of Critical Hit.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | crit_goggles |
| Item type | Equipment |
| Slot | Trinket |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Combat Power | 20 |

## Traits

| Trait |
| --- |
| [Critical Hit](trait-CriticalHit.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Assassin's Goggles](recipe-crit_goggles.md) | [Inventor](building-Inventor.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_56\"",
  "Slot": "EquipmentSlot.Trinket",
  "BaseStats": "new StatSet { (stat: EquipStat.CombatPower, amt: 20) }",
  "EquipTrait": "AdventurerTrait.CriticalHit"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:241`
