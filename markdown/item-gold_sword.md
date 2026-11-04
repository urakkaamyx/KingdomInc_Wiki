# Ceremonial Sword

Not a suitable combat weapon as-is, but its brilliant shine will surely draw attention.

## In the game

Not a suitable combat weapon as-is, but its brilliant shine will surely draw attention.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | gold_sword |
| Item type | Weapon |
| Weapon Type | Sword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 50 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ceremonial Sword](recipe-gold_sword.md) | [Blacksmith](building-Blacksmith.md) | 3.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_106\"",
  "WeaponType": "WeaponType.Sword",
  "BaseStats": "new StatSet { (stat: EquipStat.Strength, amt: 50) }"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier3.cs:133`
