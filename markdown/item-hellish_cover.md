# Malignant Cover

Tiny needles hook into the wearer's flesh, causing immense discomfort but somehow also making almost any movement more graceful and deadly.

## In the game

Tiny needles hook into the wearer's flesh, causing immense discomfort but somehow also making almost any movement more graceful and deadly.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | hellish_cover |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Medium |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 120 |
| Dexterity | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Malignant Cover](recipe-hellish_cover.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_8\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Medium",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 120),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:203`
