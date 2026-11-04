# Arcanite Claymore

The blade appears clumsy and cumbersome, but is surprisingly versatile in combat.

## In the game

The blade appears clumsy and cumbersome, but is surprisingly versatile in combat.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | arcanium_greatsword |
| Item type | Weapon |
| Weapon Type | Greatsword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 200 |
| Dexterity | 70 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Arcanite Claymore](recipe-arcanium_greatsword.md) | [Blacksmith](building-Blacksmith.md) | 4.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Summon Arbiter](recipe-summon_arbiter.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_13\"",
  "WeaponType": "WeaponType.Greatsword",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 200),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 70)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:93`
