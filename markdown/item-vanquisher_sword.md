# Vanquisher's Sword

Dark matter particles drift off its edge and embed themselves into the wounds of its victims, inflicting more suffering over time.

## In the game

Dark matter particles drift off its edge and embed themselves into the wounds of its victims, inflicting more suffering over time.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | vanquisher_sword |
| Item type | Weapon |
| Weapon Type | Sword |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Strength | 240 |
| Health | 90 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Vanquisher's Sword](recipe-vanquisher_sword.md) | [Shrine](building-Shrine.md) | 7.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_24\"",
  "WeaponType": "WeaponType.Sword",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Strength, amt: 240),\n\t\t\t\t(stat: EquipStat.Health, amt: 90)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier11.cs:269`
