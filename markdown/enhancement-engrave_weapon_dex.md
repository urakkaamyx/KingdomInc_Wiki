# Engrave Weapon: Dexterity

Engrave any weapon to provide additional Dexterity.

## Effect

Engrave any weapon to provide additional Dexterity.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Dexterity | 30 |

## Properties

| Property | Value |
| --- | --- |
| Type | Engrave |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Engrave Weapon: Dexterity](recipe-engrave_weapon_dex.md) | [Engraver](building-Engraver.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_94\"",
  "Type": "EnhancementType.Engrave",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Dexterity,\n\t\t\t\t30\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Engraver.cs:87`
