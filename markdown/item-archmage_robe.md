# Archmage's Robe

Stylish and gaudy, this magnificent robe is sure to awe anyone that sees you wearing it. No harm ever came from trying on some clothes, right?

## In the game

Stylish and gaudy, this magnificent robe is sure to awe anyone that sees you wearing it. No harm ever came from trying on some clothes, right?

## Reference values

| Property | Value |
| --- | --- |
| Item ID | archmage_robe |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 60 |
| Magic | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Archmage's Robe](recipe-archmage_robe.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_12\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 60),\n\t\t\t\t(stat: EquipStat.Magic, amt: 100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:247`
