# Elixir of Mastery

After drinking this concoction the user feels ever so slightly more proficient at anything they do.

## In the game

After drinking this concoction the user feels ever so slightly more proficient at anything they do.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | stats_potion |
| Item type | Equipment |
| Slot | Potion |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 36 |
| Dexterity | 36 |
| Magic | 36 |
| Wisdom | 36 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Elixir of Mastery](recipe-stats_potion.md) | [Alchemist](building-Alchemist.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Manual of Self-Improvement](recipe-tome_of_stats.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_156\"",
  "Slot": "EquipmentSlot.Potion",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Strength,\n\t\t\t\t\t36\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Dexterity,\n\t\t\t\t\t36\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Magic,\n\t\t\t\t\t36\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Wisdom,\n\t\t\t\t\t36\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier9.cs:59`
