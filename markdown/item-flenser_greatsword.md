# Flenser's Sword

A blade from the deepest pits of hell. It subtly encourages the wielder to commit horrible atrocities.

## In the game

A blade from the deepest pits of hell. It subtly encourages the wielder to commit horrible atrocities.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | flenser_greatsword |
| Item type | Weapon |
| Weapon Type | Greatsword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 400 |
| Health | 140 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Flenser's Sword](recipe-flenser_greatsword.md) | [Shrine](building-Shrine.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_16\"",
  "WeaponType": "WeaponType.Greatsword",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 400),\n\t\t\t\t(stat: EquipStat.Health, amt: 140)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:299`
