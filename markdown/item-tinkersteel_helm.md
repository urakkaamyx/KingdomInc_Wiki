# Tinkersteel Helm

The continuous clicking of tiny gears slowly drives the wearer insane, but also serves to keep them focused.

## In the game

The continuous clicking of tiny gears slowly drives the wearer insane, but also serves to keep them focused.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tinkersteel_helm |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 110 |
| Health | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Tinkersteel Helm](recipe-tinkersteel_helm.md) | [Blacksmith](building-Blacksmith.md) | 5.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Demonsteel Helm](recipe-demonsteel_helm.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_1\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 110),\n\t\t\t\t(stat: EquipStat.Health, amt: 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:60`
