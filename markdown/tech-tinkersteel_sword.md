# Tinkersteel Sword

The sword will sometimes abruptly change direction in combat to strike from an unexpected angle.

## Research effect

The sword will sometimes abruptly change direction in combat to strike from an unexpected angle.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tinkersteel_sword |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Tinkersteel Sword](item-tinkersteel_sword.md) |

## Related recipe

| Recipe |
| --- |
| [Tinkersteel Sword](recipe-tinkersteel_sword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons3_23\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:170`
- `Assets.Source.Player/TechNode.cs:1`
