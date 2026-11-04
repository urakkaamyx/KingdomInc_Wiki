# Enchant Armor: Stats

Enchants any piece of Head or Chest armor to provide boosts to all primary stats.

## Effect

Enchants any piece of Head or Chest armor to provide boosts to all primary stats.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Strength | 20 |
| Dexterity | 20 |
| Magic | 20 |
| Wisdom | 20 |

## Properties

| Property | Value |
| --- | --- |
| Type | Enchant |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Enchant Armor: Stats](recipe-enchant_armor_stats.md) | [Enchanter](building-Enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_96\"",
  "Type": "EnhancementType.Enchant",
  "Stats": "new StatSet\n\t\t\t{\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Strength,\n\t\t\t\t\t20\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Dexterity,\n\t\t\t\t\t20\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Magic,\n\t\t\t\t\t20\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\tEquipStat.Wisdom,\n\t\t\t\t\t20\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Enchanter.cs:57`
