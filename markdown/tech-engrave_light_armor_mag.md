# Embroider Clothing: Magic

Embroider a piece of light or medium armor to provide additional Magic.

## Research effect

Embroider a piece of light or medium armor to provide additional Magic.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_light_armor_mag |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Harvest Mushrooms](tech-forest_mushroom.md) |

## Related recipe

| Recipe |
| --- |
| [Embroider Clothing: Magic](recipe-engrave_light_armor_mag.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest_mushroom\" }",
  "IconName": "\"Icons_99\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:69`
- `Assets.Source.Player/TechNode.cs:1`
