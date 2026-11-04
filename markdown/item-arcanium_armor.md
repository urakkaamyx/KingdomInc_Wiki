# Arcanite Chestguard

If you're going into battle, you might as well do it in style.

## In the game

If you're going into battle, you might as well do it in style.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | arcanium_armor |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 120 |
| Strength | 40 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Arcanite Chestguard](recipe-arcanium_armor.md) | [Blacksmith](building-Blacksmith.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_17\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 120),\n\t\t\t\t(stat: EquipStat.Strength, amt: 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:51`
