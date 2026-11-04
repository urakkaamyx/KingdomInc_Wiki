# Initiate's Hat

Often given to young wizards during their training at the school of magic.

## In the game

Often given to young wizards during their training at the school of magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | initiate_hat |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 12 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Initiate's Hat](recipe-initiate_hat.md) | [Tailor](building-Tailor.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_43\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 12) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:50`
