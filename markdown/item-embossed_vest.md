# Embossed Vest

The innate enchantments on this vest serve to increase the wearer's freedom of movement.

## In the game

The innate enchantments on this vest serve to increase the wearer's freedom of movement.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | embossed_vest |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Medium |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 80 |
| Dexterity | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Embossed Vest](recipe-embossed_vest.md) | [Leatherworker](building-Leatherworker.md) | 3.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_34\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Medium",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 80),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 50)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:162`
