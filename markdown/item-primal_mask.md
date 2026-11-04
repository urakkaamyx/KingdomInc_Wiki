# Primal Mask

Donning this mask for a prolonged period of time slowly drives the wearer mad with bloodlust.

## In the game

Donning this mask for a prolonged period of time slowly drives the wearer mad with bloodlust.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | primal_mask |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Medium |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 65 |
| Dexterity | 75 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Primal Mask](recipe-primal_mask.md) | [Leatherworker](building-Leatherworker.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Malignant Mask](recipe-hellish_mask.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_5\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Medium",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 65),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 75)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:177`
