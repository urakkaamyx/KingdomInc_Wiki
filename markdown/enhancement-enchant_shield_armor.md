# Enchant Shield - Protection

Enchants any Shield to provide additional armor.

## Effect

Enchants any Shield to provide additional armor.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Armor | 85 |

## Properties

| Property | Value |
| --- | --- |
| Type | Enchant |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Enchant Shield - Protection](recipe-enchant_shield_armor.md) | [Enchanter](building-Enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_97\"",
  "Type": "EnhancementType.Enchant",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Armor,\n\t\t\t\t85\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Enchanter.cs:81`
