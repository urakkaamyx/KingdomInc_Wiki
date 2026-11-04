# Medallion of Excellence

A talisman normally awarded to exceptionally gifted adventurers after a lifetime of service to the guild.

## In the game

A talisman normally awarded to exceptionally gifted adventurers after a lifetime of service to the guild.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | stats_amulet |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 42 |
| Dexterity | 42 |
| Magic | 42 |
| Wisdom | 42 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Medallion of Excellence](recipe-stats_amulet.md) | [Jeweler](building-Jeweler.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_216\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 42),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 42),\n\t\t\t\t(stat: EquipStat.Magic, amt: 42),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 42)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:286`
