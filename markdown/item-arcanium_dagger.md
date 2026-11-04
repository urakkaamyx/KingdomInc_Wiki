# Arcanite Backstabber

Its thin blade easily passes through even the sturdiest armor without snapping.

## In the game

Its thin blade easily passes through even the sturdiest armor without snapping.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | arcanium_dagger |
| Item type | Weapon |
| Weapon Type | Dagger |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 120 |
| Health | 40 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Arcanite Backstabber](recipe-arcanium_dagger.md) | [Blacksmith](building-Blacksmith.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_14\"",
  "WeaponType": "WeaponType.Dagger",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 120),\n\t\t\t\t(stat: EquipStat.Health, amt: 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:83`
