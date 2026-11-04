# Scholar's Hat

The mark of a true intellectual, and a symbol of authority in wizarding cliques.

## In the game

The mark of a true intellectual, and a symbol of authority in wizarding cliques.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | cotton_hat |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 24 |
| Magic | 40 |
| Wisdom | 40 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Scholar's Hat](recipe-cotton_hat.md) | [Tailor](building-Tailor.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_33\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 24),\n\t\t\t\t(stat: EquipStat.Magic, amt: 40),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:150`
