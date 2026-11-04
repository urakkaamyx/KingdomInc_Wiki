# Iron Armor

Heavy and not very comfortable to wear, but provides sufficient protection at low cost.

## In the game

Heavy and not very comfortable to wear, but provides sufficient protection at low cost.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | iron_armor |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Iron Armor](recipe-iron_armor.md) | [Blacksmith](building-Blacksmith.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_26\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 60) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier1.cs:28`
