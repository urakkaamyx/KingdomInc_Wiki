# Ring of Strength

An ornate ring adorned with a radiant topaz.

## In the game

An ornate ring adorned with a radiant topaz.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ring_of_strength |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ring of Strength](recipe-ring_of_strength.md) | [Jeweler](building-Jeweler.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Band of the Cyclops](recipe-ring_of_strength_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_204\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Strength, amt: 50) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:59`
