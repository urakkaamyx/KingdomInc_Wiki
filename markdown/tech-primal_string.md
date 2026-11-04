# Primal String

A flexible ribbon cut from a single piece of treated animal hide.

## Research effect

A flexible ribbon cut from a single piece of treated animal hide.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | primal_string |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Leatherworker](tech-leatherworker.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Primal String](item-primal_string.md) |

## Related recipe

| Recipe |
| --- |
| [Primal String](recipe-primal_string.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"leatherworker\"",
  "IconName": "\"Icons3_35\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Leatherworker.cs:70`
- `Assets.Source.Player/TechNode.cs:1`
