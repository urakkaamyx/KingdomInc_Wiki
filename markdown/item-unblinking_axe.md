# Cyclopean Battleaxe

The malignant growth overtaking this axe has manifested as a giant, unblinking eye, staring at its enemies with unrestrained fury.

## In the game

The malignant growth overtaking this axe has manifested as a giant, unblinking eye, staring at its enemies with unrestrained fury.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | unblinking_axe |
| Item type | Weapon |
| Weapon Type | Battleaxe |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 400 |
| Health | 140 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Cyclopean Battleaxe](recipe-unblinking_axe.md) | [Shrine](building-Shrine.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_20\"",
  "WeaponType": "WeaponType.Battleaxe",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 400),\n\t\t\t\t(stat: EquipStat.Health, amt: 140)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:309`
