# Iron Greatsword

A huge blade that still feels surprisingly maneuverable in the right hands.

## In the game

A huge blade that still feels surprisingly maneuverable in the right hands.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | iron_greatsword |
| Item type | Weapon |
| Weapon Type | Greatsword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 100 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Iron Greatsword](recipe-iron_greatsword.md) | [Blacksmith](building-Blacksmith.md) | 4.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_54\"",
  "WeaponType": "WeaponType.Greatsword",
  "BaseStats": "new StatSet { (stat: EquipStat.Strength, amt: 100) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier2.cs:103`
