# Embroider Clothing: Health

Embroider a piece of light or medium armor to provide a minor Health bonus.

## Effect

Embroider a piece of light or medium armor to provide a minor Health bonus.

## Base stat modifiers

Enhancement quality and application rules determine the final contribution.

| Stat | Amount at definition quality |
| --- | --- |
| Health | 30 |

## Properties

| Property | Value |
| --- | --- |
| Type | Engrave |

## Application recipes

| Recipe | Station |
| --- | --- |
| [Embroider Clothing: Health](recipe-engrave_light_armor_health.md) | [Engraver](building-Engraver.md) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_93\"",
  "Type": "EnhancementType.Engrave",
  "Stats": "new StatSet { \n\t\t\t{\n\t\t\t\tEquipStat.Health,\n\t\t\t\t30\n\t\t\t} }"
}
```

</details>

## Sources

- `Assets.Source.Items.Enhancements/Engraver.cs:17`
