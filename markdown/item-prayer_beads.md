# Prayer Beads

An ornate necklace of blessed gold and silver beads, intended to be used in ritualized prayer.

## In the game

An ornate necklace of blessed gold and silver beads, intended to be used in ritualized prayer.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | prayer_beads |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 20 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Prayer Beads](recipe-prayer_beads.md) | [Jeweler](building-Jeweler.md) | 4.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Blessed Prayer Beads](recipe-blessed_prayer_beads.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_70\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Wisdom,\n\t\t\t\t20\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:11`
