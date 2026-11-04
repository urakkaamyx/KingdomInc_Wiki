# Tinkersteel Battleaxe

The weapon's mass appears to increase significantly before impact, inflicting both slashing and bludgeoning mayhem.

## In the game

The weapon's mass appears to increase significantly before impact, inflicting both slashing and bludgeoning mayhem.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tinkersteel_axe |
| Item type | Weapon |
| Weapon Type | Battleaxe |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 300 |
| Health | 105 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Tinkersteel Battleaxe](recipe-tinkersteel_axe.md) | [Blacksmith](building-Blacksmith.md) | 9.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Cyclopean Battleaxe](recipe-unblinking_axe.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_19\"",
  "WeaponType": "WeaponType.Battleaxe",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 300),\n\t\t\t\t(stat: EquipStat.Health, amt: 105)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:111`
