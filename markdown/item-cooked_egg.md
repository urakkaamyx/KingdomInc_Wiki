# Hardboiled Egg

Not the tastiest meal, but it'll fill your stomach in a pinch.

## In the game

Not the tastiest meal, but it'll fill your stomach in a pinch.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | cooked_egg |
| Item type | Equipment |
| Slot | Food |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 25 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Hardboiled Egg](recipe-cooked_egg.md) | [Campfire](building-Campfire.md) | 8.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Simple Salad](recipe-salad.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_79\"",
  "Slot": "EquipmentSlot.Food",
  "BaseStats": "new StatSet { (stat: EquipStat.Dexterity, amt: 25) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier4.cs:51`
