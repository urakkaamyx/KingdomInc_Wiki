# Dark Prophet's Robe

A beguiling aura draws the attention of allies and foes alike, turning even the most hardened skeptic into a devout follower.

## In the game

A beguiling aura draws the attention of allies and foes alike, turning even the most hardened skeptic into a devout follower.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | prophet_robe |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 60 |
| Wisdom | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Dark Prophet's Robe](recipe-prophet_robe.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_14\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 60),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:225`
