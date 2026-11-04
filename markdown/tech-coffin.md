# Coffin

A sturdy wooden box designed to hold the dead body of a human.

## Research effect

A sturdy wooden box designed to hold the dead body of a human.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | coffin |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Graveyard](tech-graveyard.md) |

## Related item

| Item |
| --- |
| [Coffin](item-coffin.md) |

## Related recipe

| Recipe |
| --- |
| [Coffin](recipe-coffin.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"carpenter\"",
  "CostTier": "11",
  "AdditionalRequirements": "new List<string> { \"graveyard\" }",
  "IconName": "\"Icons2_80\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Carpenter.cs:149`
- `Assets.Source.Player/TechNode.cs:1`
