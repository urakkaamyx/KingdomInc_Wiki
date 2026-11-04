# Stalker Stew

Deliciously oniony. Just don't ask about the other ingredient.

## In the game

Deliciously oniony. Just don't ask about the other ingredient.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | stalker_stew |
| Item type | Equipment |
| Slot | Food |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Magic | 45 |
| Wisdom | 45 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Stalker Stew](recipe-stalker_stew.md) | [Kitchen](building-Kitchen.md) | 6.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_179\"",
  "Slot": "EquipmentSlot.Food",
  "BaseStats": "new StatSet\n\t\t\t{\n\t\t\t\t(stat: EquipStat.Magic, amt: 45),\n\t\t\t\t(stat: EquipStat.Wisdom, amt: 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier7.cs:92`
