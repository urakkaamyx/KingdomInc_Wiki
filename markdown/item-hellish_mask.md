# Malignant Mask

The mask slowly grows over the wearer's face, replacing their human features with a horrifying demonic visage.

## In the game

The mask slowly grows over the wearer's face, replacing their human features with a horrifying demonic visage.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | hellish_mask |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Medium |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 75 |
| Dexterity | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Malignant Mask](recipe-hellish_mask.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_6\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Medium",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 75),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:214`
