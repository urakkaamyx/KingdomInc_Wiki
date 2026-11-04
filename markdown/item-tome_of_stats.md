# Manual of Self-Improvement

Describes a hundred daily habits to improve the reader's life in almost every way possible.

## In the game

Describes a hundred daily habits to improve the reader's life in almost every way possible.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tome_of_stats |
| Item type | Equipment |
| Slot | Scroll |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 50 |
| Dexterity | 50 |
| Magic | 50 |
| Wisdom | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Manual of Self-Improvement](recipe-tome_of_stats.md) | [Scribe](building-Scribe.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_65\"",
  "Slot": "EquipmentSlot.Scroll",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 50),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 50),\n\t\t\t\t(stat: EquipStat.Magic, amt: 50),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 50)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:380`
