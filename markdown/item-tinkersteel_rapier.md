# Tinkersteel Rapier

The impossibly light blade darts through the air as if it's teleporting, slicing through its victims without slowing down.

## In the game

The impossibly light blade darts through the air as if it's teleporting, slicing through its victims without slowing down.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tinkersteel_rapier |
| Item type | Weapon |
| Weapon Type | Rapier |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 240 |
| Health | 60 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Tinkersteel Rapier](recipe-tinkersteel_rapier.md) | [Blacksmith](building-Blacksmith.md) | 7.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Ethereal Rapier](recipe-blink_rapier.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_21\"",
  "WeaponType": "WeaponType.Rapier",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 240),\n\t\t\t\t(stat: EquipStat.Health, amt: 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:91`
