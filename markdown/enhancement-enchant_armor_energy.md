# Enchant Armor: Vigor

Enchants any piece of Head or Chest armor to provide additional Energy.

## Effect

Enchants any piece of Head or Chest armor to provide additional Energy.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Energy | 16 |

## Properties

| Property | Value |
| --- | --- |
| Type | Enchant |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Enchant Armor: Vigor](recipe-enchant_armor_energy.md) | [Enchanter](building-Enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_53\"",
  "Type": "EnhancementType.Enchant",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Energy,\n\t\t\t\t16\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Enchanter.cs:25`
