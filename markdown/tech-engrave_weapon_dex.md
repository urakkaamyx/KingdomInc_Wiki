# Engrave Weapon: Dexterity

Engrave any weapon to provide additional Dexterity.

## Research effect

Engrave any weapon to provide additional Dexterity.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_weapon_dex |
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
| [Engrave Weapon: Dexterity](recipe-engrave_weapon_dex.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest_resin\" }",
  "IconName": "\"Icons_94\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:90`
- `Assets.Source.Player/TechNode.cs:1`
