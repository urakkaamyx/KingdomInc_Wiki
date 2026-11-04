# Primal Cover

The shimmering surface of this armor serves to obscure the wearer's movements.

## In the game

The shimmering surface of this armor serves to obscure the wearer's movements.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | primal_cover |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Medium |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 110 |
| Dexterity | 75 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Primal Cover](recipe-primal_cover.md) | [Leatherworker](building-Leatherworker.md) | 3.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Malignant Cover](recipe-hellish_cover.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_7\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Medium",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 110),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 75)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:166`
