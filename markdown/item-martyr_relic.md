# Relic of the Martyr

The bones of a fallen hero, carefully preserved in a gilded wooden locket. Bestows divine protection upon the bearer.

## In the game

The bones of a fallen hero, carefully preserved in a gilded wooden locket. Bestows divine protection upon the bearer.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | martyr_relic |
| Item type | Equipment |
| Slot | Trinket |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 90 |

## Traits

| Trait |
| --- |
| [Divine Protection2](trait-DivineProtection2.md) |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Relic of the Martyr](recipe-martyr_relic.md) | [Shrine](building-Shrine.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_78\"",
  "Slot": "EquipmentSlot.Trinket",
  "BaseStats": "new StatSet { (stat: EquipStat.Health, amt: 90) }",
  "EquipTrait": "AdventurerTrait.DivineProtection2"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:421`
