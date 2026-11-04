# Tinkersteel Greatsword

Even though the edge doesn't seem to be particularly sharp, it still slices through almost anything with ease.

## In the game

Even though the edge doesn't seem to be particularly sharp, it still slices through almost anything with ease.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | tinkersteel_greatsword |
| Item type | Weapon |
| Weapon Type | Greatsword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 300 |
| Dexterity | 105 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Tinkersteel Greatsword](recipe-tinkersteel_greatsword.md) | [Blacksmith](building-Blacksmith.md) | 9.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Flenser's Sword](recipe-flenser_greatsword.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_15\"",
  "WeaponType": "WeaponType.Greatsword",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 300),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 105)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:101`
