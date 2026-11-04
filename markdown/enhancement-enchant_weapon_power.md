# Enchant Weapon: Power

Enchants an weapon to provide additional Combat Power.

## Effect

Enchants an weapon to provide additional Combat Power.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Combat Power | 92 |

## Properties

| Property | Value |
| --- | --- |
| Type | Enchant |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Enchant Weapon: Power](recipe-enchant_weapon_power.md) | [Enchanter](building-Enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_52\"",
  "Type": "EnhancementType.Enchant",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.CombatPower,\n\t\t\t\t92\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Enchanter.cs:15`
