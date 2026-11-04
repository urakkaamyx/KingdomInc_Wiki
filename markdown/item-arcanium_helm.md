# Arcanite Casque

A helmet fit for a champion.

## In the game

A helmet fit for a champion.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | arcanium_helm |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 80 |
| Health | 40 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Arcanite Casque](recipe-arcanium_helm.md) | [Blacksmith](building-Blacksmith.md) | 2.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_16\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 80),\n\t\t\t\t(stat: EquipStat.Health, amt: 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:62`
