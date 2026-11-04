# Engraved Jewelry

A simple but delicate engraving of power that gives a small quality boost.

## Research effect

A simple but delicate engraving of power that gives a small quality boost.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engrave_jewelry_quality |
| Type | Recipe |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Jeweler](tech-jeweler.md) |

## Related recipe

| Recipe |
| --- |
| [Engraved Jewelry](recipe-engrave_jewelry_quality.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"engraver\"",
  "CostTier": "8",
  "AdditionalRequirements": "new List<string> { \"jeweler\" }",
  "IconName": "\"Icons3_98\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:127`
- `Assets.Source.Player/TechNode.cs:1`
