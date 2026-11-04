# Demonsteel Armor

Blood drips continuously from tiny holes in the armor's surface with no indication of where it's coming from.

## In the game

Blood drips continuously from tiny holes in the armor's surface with no indication of where it's coming from.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | demonsteel_armor |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 180 |
| Strength | 80 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Demonsteel Armor](recipe-demonsteel_armor.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_4\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 180),\n\t\t\t\t(stat: EquipStat.Strength, amt: 80)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:170`
