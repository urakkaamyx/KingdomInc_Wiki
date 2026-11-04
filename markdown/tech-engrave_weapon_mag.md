# Engrave Weapon: Magic

Engrave any weapon to provide additional Magic.

## Research effect

Engrave any weapon to provide additional Magic.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_weapon_mag |
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
| [Engrave Weapon: Magic](recipe-engrave_weapon_mag.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest_mushroom\" }",
  "IconName": "\"Icons_95\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:97`
- `Assets.Source.Player/TechNode.cs:1`
