# Stoneskin Elixir

A disgustingly bitter potion. Shortly after consumption, the drinker feels impervious to harm.

## In the game

A disgustingly bitter potion. Shortly after consumption, the drinker feels impervious to harm.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | armor_potion |
| Item type | Equipment |
| Slot | Potion |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 62 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Stoneskin Elixir](recipe-armor_potion.md) | [Alchemist](building-Alchemist.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_154\"",
  "Slot": "EquipmentSlot.Potion",
  "BaseStats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Armor,\n\t\t\t\t62\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier9.cs:43`
