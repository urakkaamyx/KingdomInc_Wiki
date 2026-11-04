# Tinkersteel Armor

The mago-tech folded into this armor serve to deflect blows and dampen impacts.

## In the game

The mago-tech folded into this armor serve to deflect blows and dampen impacts.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tinkersteel_armor |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 160 |
| Strength | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Tinkersteel Armor](recipe-tinkersteel_armor.md) | [Blacksmith](building-Blacksmith.md) | 6.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Demonsteel Armor](recipe-demonsteel_armor.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_3\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 160),\n\t\t\t\t(stat: EquipStat.Strength, amt: 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:49`
