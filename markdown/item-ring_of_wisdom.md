# Ring of Wisdom

A graceful ring adorned with a majestic diamond.

## In the game

A graceful ring adorned with a majestic diamond.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ring_of_wisdom |
| Item type | Equipment |
| Slot | Ring |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ring of Wisdom](recipe-ring_of_wisdom.md) | [Jeweler](building-Jeweler.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Band of Tranquility](recipe-ring_of_wisdom_2.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_203\"",
  "Slot": "EquipmentSlot.Ring",
  "BaseStats": "new StatSet { (stat: EquipStat.Wisdom, amt: 50) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:77`
