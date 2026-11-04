# Mushroom Stew

A hearty stew that fortifies both body and mind. Overconsumption may lead to hallucinations.

## In the game

A hearty stew that fortifies both body and mind. Overconsumption may lead to hallucinations.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | mushroom_stew |
| Item type | Equipment |
| Slot | Food |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 30 |
| Strength | 10 |
| Dexterity | 10 |
| Magic | 10 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Mushroom Stew](recipe-mushroom_stew.md) | [Campfire](building-Campfire.md) | 5.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_129\"",
  "Slot": "EquipmentSlot.Food",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Health, amt: 30),\n\t\t\t\t(stat: EquipStat.Strength, amt: 10),\n\t\t\t\t(stat: EquipStat.Dexterity, amt: 10),\n\t\t\t\t(stat: EquipStat.Magic, amt: 10)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier4.cs:84`
