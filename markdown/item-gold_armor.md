# Parade Armor

A suit of armor made not for protection, but for showing off your wealth and status.

## In the game

A suit of armor made not for protection, but for showing off your wealth and status.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | gold_armor |
| Item type | Equipment |
| Slot | Chest |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Parade Armor](recipe-gold_armor.md) | [Blacksmith](building-Blacksmith.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Summon Valkyrie](recipe-summon_valkyrie.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_107\"",
  "Slot": "EquipmentSlot.Chest",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 50) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier3.cs:119`
