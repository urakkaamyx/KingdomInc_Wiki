# Iron Dagger

A simple iron dagger, for anyone wishing to train in the more subtle forms of combat.

## In the game

A simple iron dagger, for anyone wishing to train in the more subtle forms of combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | iron_dagger |
| Item type | Weapon |
| Weapon Type | Dagger |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Iron Dagger](recipe-iron_dagger.md) | [Blacksmith](building-Blacksmith.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_7\"",
  "WeaponType": "WeaponType.Dagger",
  "BaseStats": "new StatSet { (stat: EquipStat.Dexterity, amt: 60) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier1.cs:48`
