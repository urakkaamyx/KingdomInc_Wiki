# Archbishop's Staff

An honorable weapon of the high clergy. Its overwhelming presence demands both reverence and obedience.

## Research effect

An honorable weapon of the high clergy. Its overwhelming presence demands both reverence and obedience.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | archbishop_staff |
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
| [Archbishop's Staff](item-archbishop_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Archbishop's Staff](recipe-archbishop_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }",
  "IconName": "\"Icons3_31\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:141`
- `Assets.Source.Player/TechNode.cs:1`
