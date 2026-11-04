# Engrave Heavy Armor: Defense

Engrave a piece of heavy armor to provide additional Armor.

## Research effect

Engrave a piece of heavy armor to provide additional Armor.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_heavy_armor_armor |
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
| [Engrave Heavy Armor: Defense](recipe-engrave_heavy_armor_armor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest_bone\" }",
  "IconName": "\"Icons_97\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:48`
- `Assets.Source.Player/TechNode.cs:1`
