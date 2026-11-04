# Embroider Clothing: Wisdom

Embroider a piece of light or medium armor to provide additional Wisdom.

## Research effect

Embroider a piece of light or medium armor to provide additional Wisdom.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_light_armor_wis |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Forest](tech-forest.md) |

## Related recipe

| Recipe |
| --- |
| [Embroider Clothing: Wisdom](recipe-engrave_light_armor_wis.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest\" }",
  "IconName": "\"Icons_100\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:76`
- `Assets.Source.Player/TechNode.cs:1`
