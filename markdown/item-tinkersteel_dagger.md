# Tinkersteel Dagger

A nimble, telescopic blade. The blade extends after puncturing the target, causing extensive internal damage.

## In the game

A nimble, telescopic blade. The blade extends after puncturing the target, causing extensive internal damage.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tinkersteel_dagger |
| Item type | Weapon |
| Weapon Type | Dagger |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 180 |
| Health | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Tinkersteel Dagger](recipe-tinkersteel_dagger.md) | [Blacksmith](building-Blacksmith.md) | 6.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Blighted Dagger](recipe-blighted_dagger.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_17\"",
  "WeaponType": "WeaponType.Dagger",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 180),\n\t\t\t\t(stat: EquipStat.Health, amt: 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:81`
