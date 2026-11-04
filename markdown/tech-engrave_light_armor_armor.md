# Embroider Clothing: Defense

Embroider a piece of light or medium armor to provide additional Armor.

## Research effect

Embroider a piece of light or medium armor to provide additional Armor.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_light_armor_armor |
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
| [Embroider Clothing: Defense](recipe-engrave_light_armor_armor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "AdditionalRequirements": "new List<string> { \"forest_bone\" }",
  "IconName": "\"Icons_101\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:55`
- `Assets.Source.Player/TechNode.cs:1`
