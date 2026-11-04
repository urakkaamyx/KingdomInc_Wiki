# Rough Vest

The durable leather hide, while low quality, provides adequate protection in combat.

## In the game

The durable leather hide, while low quality, provides adequate protection in combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | rough_vest |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Medium |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 40 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Rough Vest](recipe-rough_vest.md) | [Leatherworker](building-Leatherworker.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_44\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Medium",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 40) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:57`
