# Embroider Clothing: Wisdom

Embroider a piece of light or medium armor to provide additional Wisdom.

## Effect

Embroider a piece of light or medium armor to provide additional Wisdom.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Wisdom | 25 |

## Properties

| Property | Value |
| --- | --- |
| Type | Engrave |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Embroider Clothing: Wisdom](recipe-engrave_light_armor_wis.md) | [Engraver](building-Engraver.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_100\"",
  "Type": "EnhancementType.Engrave",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Wisdom,\n\t\t\t\t25\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Engraver.cs:67`
