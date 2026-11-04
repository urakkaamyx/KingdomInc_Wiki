# Dark Prophet's Hood

The wearer is tormented by myriad voices screaming blasphemous prophecies into their ears.

## In the game

The wearer is tormented by myriad voices screaming blasphemous prophecies into their ears.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | prophet_hood |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 36 |
| Wisdom | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Dark Prophet's Hood](recipe-prophet_hood.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_13\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 36),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:236`
