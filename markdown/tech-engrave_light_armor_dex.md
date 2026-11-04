# Embroider Clothing: Dexterity

Embroider a piece of light or medium armor to provide additional Dexterity.

## Research effect

Embroider a piece of light or medium armor to provide additional Dexterity.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_light_armor_dex |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Harvest Resin](tech-forest_resin.md) |

## Related recipe

| Recipe |
| --- |
| [Embroider Clothing: Dexterity](recipe-engrave_light_armor_dex.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest_resin\" }",
  "IconName": "\"Icons_98\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:62`
- `Assets.Source.Player/TechNode.cs:1`
