# Softwood Plank

Freshly sawn from a softwood log, ready for further processing.

## Research effect

Freshly sawn from a softwood log, ready for further processing.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | wood_plank |
| Type | Recipe |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Forest](tech-forest.md) |

## Related item

| Item |
| --- |
| [Softwood Plank](item-wood_plank.md) |

## Related recipe

| Recipe |
| --- |
| [Softwood Plank](recipe-wood_plank.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "4",
  "AdditionalRequirements": "new List<string> { \"forest\" }",
  "IconName": "\"Icons_14\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:53`
- `Assets.Source.Player/TechNode.cs:1`
