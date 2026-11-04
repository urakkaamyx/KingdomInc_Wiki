# Puppet Shield

A clockwork arm that straps to the wearer's back, holding a small round shield. Its rudimentary mago-tech brain predicts and blocks incoming enemy attacks.

## In the game

A clockwork arm that straps to the wearer's back, holding a small round shield. Its rudimentary mago-tech brain predicts and blocks incoming enemy attacks.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | shield_arm |
| Item type | Equipment |
| Slot | Trinket |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 90 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Puppet Shield](recipe-shield_arm.md) | [Inventor](building-Inventor.md) | 2.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_54\"",
  "Slot": "EquipmentSlot.Trinket",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 90) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:254`
