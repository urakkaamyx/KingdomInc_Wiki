# Apothecary's Tome

Contains a variety of medicinal recipes and practical tips for the aspiring doctor. Medical education not required.

## In the game

Contains a variety of medicinal recipes and practical tips for the aspiring doctor. Medical education not required.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tome_of_health |
| Item type | Equipment |
| Slot | Scroll |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 90 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Apothecary's Tome](recipe-tome_of_health.md) | [Scribe](building-Scribe.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_64\"",
  "Slot": "EquipmentSlot.Scroll",
  "BaseStats": "new StatSet { (stat: EquipStat.Health, amt: 90) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:374`
