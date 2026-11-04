# Simple Wooden Shield

Will stop a sword hit or two before splitering into kindling for the night's campfire.

## In the game

Will stop a sword hit or two before splitering into kindling for the night's campfire.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | simple_wooden_shield |
| Item type | Weapon |
| Weapon Type | Shield |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 40 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Simple Wooden Shield](recipe-simple_wooden_shield.md) | [Carpenter](building-Carpenter.md) | 3.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Reinforced Wooden Shield](recipe-reinforced_wooden_shield.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_52\"",
  "WeaponType": "WeaponType.Shield",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 40) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:89`
