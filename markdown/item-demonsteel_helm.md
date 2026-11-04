# Demonsteel Helm

The incessant clicking of gears has been replaced with maddening whispers.

## In the game

The incessant clicking of gears has been replaced with maddening whispers.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | demonsteel_helm |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 120 |
| Health | 80 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Demonsteel Helm](recipe-demonsteel_helm.md) | [Scribe](building-Scribe.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_2\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 120),\n\t\t\t\t(stat: EquipStat.Health, amt: 80)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:181`
