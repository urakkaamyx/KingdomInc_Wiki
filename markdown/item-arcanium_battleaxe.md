# Arcanite Cleaver

For the mighty warrior that wants to fell trees and foes at the same time.

## In the game

For the mighty warrior that wants to fell trees and foes at the same time.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | arcanium_battleaxe |
| Item type | Weapon |
| Weapon Type | Battleaxe |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 200 |
| Health | 70 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Arcanite Cleaver](recipe-arcanium_battleaxe.md) | [Blacksmith](building-Blacksmith.md) | 4.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_15\"",
  "WeaponType": "WeaponType.Battleaxe",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 200),\n\t\t\t\t(stat: EquipStat.Health, amt: 70)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:103`
