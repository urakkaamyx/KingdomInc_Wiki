# Engrave Weapon: Wisdom

Engrave any weapon to provide additional Wisdom.

## Research effect

Engrave any weapon to provide additional Wisdom.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_weapon_wis |
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
| [Engrave Weapon: Wisdom](recipe-engrave_weapon_wis.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest\" }",
  "IconName": "\"Icons_96\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:104`
- `Assets.Source.Player/TechNode.cs:1`
