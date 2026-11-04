# Trueshot Bow

Fired arrows correct themselves in midair to pierce the enemy's weakspots every single time.

## In the game

Fired arrows correct themselves in midair to pierce the enemy's weakspots every single time.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | trueshot_bow |
| Item type | Weapon |
| Weapon Type | Bow |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 300 |
| Health | 105 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Trueshot Bow](recipe-trueshot_bow.md) | [Carpenter](building-Carpenter.md) | 3.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Deadeye Bow](recipe-deadeye_bow.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_25\"",
  "WeaponType": "WeaponType.Bow",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 300),\n\t\t\t\t(stat: EquipStat.Health, amt: 105)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:121`
