# Arcanite Blade

The magical properties of this sword cause its edge to always stay razor-sharp.

## In the game

The magical properties of this sword cause its edge to always stay razor-sharp.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | arcanium_sword |
| Item type | Weapon |
| Weapon Type | Sword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 120 |
| Dexterity | 40 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Arcanite Blade](recipe-arcanium_sword.md) | [Blacksmith](building-Blacksmith.md) | 3.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_12\"",
  "WeaponType": "WeaponType.Sword",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 120),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:73`
