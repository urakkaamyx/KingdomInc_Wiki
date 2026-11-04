# Engrave Weapon: Wisdom

Engrave any weapon to provide additional Wisdom.

## Effect

Engrave any weapon to provide additional Wisdom.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Wisdom | 30 |

## Properties

| Property | Value |
| --- | --- |
| Type | Engrave |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Engrave Weapon: Wisdom](recipe-engrave_weapon_wis.md) | [Engraver](building-Engraver.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_96\"",
  "Type": "EnhancementType.Engrave",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Wisdom,\n\t\t\t\t30\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Engraver.cs:107`
