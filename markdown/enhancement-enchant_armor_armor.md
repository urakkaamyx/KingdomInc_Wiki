# Enchant Armor - Protection

Enchants any piece of Head or Chest armor to provide additional armor.

## Effect

Enchants any piece of Head or Chest armor to provide additional armor.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Armor | 35 |

## Properties

| Property | Value |
| --- | --- |
| Type | Enchant |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Enchant Armor - Protection](recipe-enchant_armor_armor.md) | [Enchanter](building-Enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_182\"",
  "Type": "EnhancementType.Enchant",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Armor,\n\t\t\t\t35\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Enchanter.cs:47`
