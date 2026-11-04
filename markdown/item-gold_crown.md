# Sapphire Crown

An ornate piece of jewelry, sometimes worn by the aristocracy in honor of the late King.

## In the game

An ornate piece of jewelry, sometimes worn by the aristocracy in honor of the late King.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | gold_crown |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 10 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Sapphire Crown](recipe-gold_crown.md) | [Blacksmith](building-Blacksmith.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_108\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 10) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier3.cs:126`
