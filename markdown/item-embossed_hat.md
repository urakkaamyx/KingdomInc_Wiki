# Embossed Mask

Serves to obscure the wearer's identity and improve their lethality at the same time.

## In the game

Serves to obscure the wearer's identity and improve their lethality at the same time.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | embossed_hat |
| Item type | Equipment |
| Slot | Head |
| Armor Type | Medium |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 50 |
| Dexterity | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Embossed Mask](recipe-embossed_hat.md) | [Leatherworker](building-Leatherworker.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_35\"",
  "Slot": "EquipmentSlot.Head",
  "ArmorType": "ArmorType.Medium",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Armor, amt: 50),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 50)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:173`
