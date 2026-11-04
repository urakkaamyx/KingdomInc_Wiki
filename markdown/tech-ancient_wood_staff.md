# Ancient Wood Staff

Tough and unyielding, but its delicate carved patterns suggest a hidden purpose beyond raw strength.

## Research effect

Tough and unyielding, but its delicate carved patterns suggest a hidden purpose beyond raw strength.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ancient_wood_staff |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Ancient Wood Plank](tech-ancient_wood_plank.md) |

## Related item

| Item |
| --- |
| [Ancient Wood Staff](item-ancient_wood_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Ancient Wood Staff](recipe-ancient_wood_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"ancient_wood_plank\" }",
  "IconName": "\"Icons2_21\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:77`
- `Assets.Source.Player/TechNode.cs:1`
