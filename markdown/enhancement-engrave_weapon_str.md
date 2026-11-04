# Engrave Weapon: Strength

Engrave any weapon to provide additional Strength.

## Effect

Engrave any weapon to provide additional Strength.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Strength | 30 |

## Properties

| Property | Value |
| --- | --- |
| Type | Engrave |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Engrave Weapon: Strength](recipe-engrave_weapon_str.md) | [Engraver](building-Engraver.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_91\"",
  "Type": "EnhancementType.Engrave",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Strength,\n\t\t\t\t30\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Engraver.cs:77`
