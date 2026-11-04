# Iron Sword

A simple iron sword, suitable for any initiate knight or rookie adventurer.

## In the game

A simple iron sword, suitable for any initiate knight or rookie adventurer.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | iron_sword |
| Item type | Weapon |
| Weapon Type | Sword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Iron Sword](recipe-iron_sword.md) | [Blacksmith](building-Blacksmith.md) | 3.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_6\"",
  "WeaponType": "WeaponType.Sword",
  "BaseStats": "new StatSet { (stat: EquipStat.Strength, amt: 60) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier1.cs:42`
