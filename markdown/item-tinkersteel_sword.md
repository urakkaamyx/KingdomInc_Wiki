# Tinkersteel Sword

The sword will sometimes abruptly change direction in combat to strike from an unexpected angle.

## In the game

The sword will sometimes abruptly change direction in combat to strike from an unexpected angle.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tinkersteel_sword |
| Item type | Weapon |
| Weapon Type | Sword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 180 |
| Dexterity | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Tinkersteel Sword](recipe-tinkersteel_sword.md) | [Blacksmith](building-Blacksmith.md) | 7.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Vanquisher's Sword](recipe-vanquisher_sword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_23\"",
  "WeaponType": "WeaponType.Sword",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 180),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:71`
