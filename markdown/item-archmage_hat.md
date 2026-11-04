# Archmage's Hat

The kind of headwear that draws attention at a conference of mages. Subtle thought manipulation makes the wearer more adept at magic.

## In the game

The kind of headwear that draws attention at a conference of mages. Subtle thought manipulation makes the wearer more adept at magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | archmage_hat |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Light |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 36 |
| Magic | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Archmage's Hat](recipe-archmage_hat.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_10\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Light",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 36),\n\t\t\t\t(stat: EquipStat.Magic, amt: 100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:258`
