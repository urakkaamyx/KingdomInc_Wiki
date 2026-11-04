# Supple String

A flexible, braided leather cord that somehow seems almost unbreakable.

## Research effect

A flexible, braided leather cord that somehow seems almost unbreakable.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supple_string |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Leatherworker](tech-leatherworker.md) |
| [Enchanter](tech-enchanter.md) |

## Related item

| Item |
| --- |
| [Supple String](item-supple_string.md) |

## Related recipe

| Recipe |
| --- |
| [Supple String](recipe-supple_string.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"leatherworker\"",
  "CostTier": "6",
  "IconName": "\"Icons2_20\"",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Leatherworker.cs:46`
- `Assets.Source.Player/TechNode.cs:1`
