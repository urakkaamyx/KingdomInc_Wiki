# Pontiff's Ring

A coveted signet ring that signifies the wearer's high standing in the Church of Saint Ilonia.

## In the game

A coveted signet ring that signifies the wearer's high standing in the Church of Saint Ilonia.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | pontiff_ring |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 90 |

## Traits

| Trait |
| --- |
| [Divine Protection Aura](trait-DivineProtectionAura.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Pontiff's Ring](recipe-pontiff_ring.md) | [Shrine](building-Shrine.md) | 2.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_77\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Wisdom, amt: 90) }",
  "EquipTrait": "AdventurerTrait.DivineProtectionAura"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:414`
