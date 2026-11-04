# Engrave Weapon: Strength

Engrave any weapon to provide additional Strength.

## Research effect

Engrave any weapon to provide additional Strength.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_weapon_str |
| Type | Recipe |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Harvest Bone](tech-forest_bone.md) |

## Related recipe

| Recipe |
| --- |
| [Engrave Weapon: Strength](recipe-engrave_weapon_str.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest_bone\" }",
  "IconName": "\"Icons_91\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:83`
- `Assets.Source.Player/TechNode.cs:1`
