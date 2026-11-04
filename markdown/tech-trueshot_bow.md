# Trueshot Bow

Fired arrows correct themselves in midair to pierce the enemy's weakspots every single time.

## Research effect

Fired arrows correct themselves in midair to pierce the enemy's weakspots every single time.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | trueshot_bow |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Trueshot Bow](item-trueshot_bow.md) |

## Related recipe

| Recipe |
| --- |
| [Trueshot Bow](recipe-trueshot_bow.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }",
  "IconName": "\"Icons3_25\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:117`
- `Assets.Source.Player/TechNode.cs:1`
