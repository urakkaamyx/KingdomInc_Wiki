# Staff of the Wild

A simple staff that serves as a focus for nature-based divine magic.

## In the game

A simple staff that serves as a focus for nature-based divine magic.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | wild_staff |
| Item type | Weapon |
| Weapon Type | Staff |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 130 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Staff of the Wild](recipe-wild_staff.md) | [Carpenter](building-Carpenter.md) | 4.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_201\"",
  "WeaponType": "WeaponType.Staff",
  "BaseStats": "new StatSet { (stat: EquipStat.Wisdom, amt: 130) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier4.cs:96`
