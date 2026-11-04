# Hamburger

An exotic delicacy based off an ancient recipe.

## In the game

An exotic delicacy based off an ancient recipe.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | hamburger |
| Item type | Equipment |
| Slot | Food |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 45 |
| Dexterity | 45 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Hamburger](recipe-hamburger.md) | [Kitchen](building-Kitchen.md) | 6.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_193\"",
  "Slot": "EquipmentSlot.Food",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 45),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:68`
