# Softwood Bow

The materials used in this bow's construction aren't ideal, but it will do in a pinch.

## In the game

The materials used in this bow's construction aren't ideal, but it will do in a pinch.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | softwood_bow |
| Item type | Weapon |
| Weapon Type | Bow |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Softwood Bow](recipe-softwood_bow.md) | [Carpenter](building-Carpenter.md) | 3.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Skeletal Archer](recipe-skeletal_archer.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_47\"",
  "WeaponType": "WeaponType.Bow",
  "BaseStats": "new StatSet { (stat: EquipStat.Dexterity, amt: 100) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:71`
