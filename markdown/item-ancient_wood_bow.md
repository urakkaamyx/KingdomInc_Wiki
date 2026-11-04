# Ancient Wood Longbow

The flexible-yet-sturdy limbs of this bow allow for both exceptional accuracy and astonishing rapid fire.

## In the game

The flexible-yet-sturdy limbs of this bow allow for both exceptional accuracy and astonishing rapid fire.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | ancient_wood_bow |
| Item type | Weapon |
| Weapon Type | Bow |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Dexterity | 200 |
| Health | 70 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Ancient Wood Longbow](recipe-ancient_wood_bow.md) | [Carpenter](building-Carpenter.md) | 3.5 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_24\"",
  "WeaponType": "WeaponType.Bow",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 200),\n\t\t\t\t(stat: EquipStat.Health, amt: 70)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier6.cs:124`
