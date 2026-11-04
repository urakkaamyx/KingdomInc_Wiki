# Reinforced Wooden Shield

The iron borders of this shield will keep it together long enough for the bearer to stand a chance in open combat.

## In the game

The iron borders of this shield will keep it together long enough for the bearer to stand a chance in open combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | reinforced_wooden_shield |
| Item type | Weapon |
| Weapon Type | Shield |
| Armor Type | Heavy |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Armor | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Reinforced Wooden Shield](recipe-reinforced_wooden_shield.md) | [Carpenter](building-Carpenter.md) | 2.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_53\"",
  "WeaponType": "WeaponType.Shield",
  "ArmorType": "ArmorType.Heavy",
  "BaseStats": "new StatSet { (stat: EquipStat.Armor, amt: 60) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:96`
