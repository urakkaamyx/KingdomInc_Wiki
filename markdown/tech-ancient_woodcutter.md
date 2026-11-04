# Ancient Woodcutter

A sawblade imbued with magical fortitude, designed to cut even the most resilient logs.

## Research effect

A sawblade imbued with magical fortitude, designed to cut even the most resilient logs.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | ancient_woodcutter |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Enchanter](tech-enchanter.md) |

## Related item

| Item |
| --- |
| [Ancient Woodcutter](item-ancient_woodcutter.md) |

## Related recipe

| Recipe |
| --- |
| [Ancient Woodcutter](recipe-ancient_woodcutter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons2_8\"",
  "CostTier": "6",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:98`
- `Assets.Source.Player/TechNode.cs:1`
