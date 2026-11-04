# Participation Trophy

Inserting any soldier into a War Effort has a 5% chance of immediately granting a Medal.

## Research effect

Inserting any soldier into a War Effort has a 5% chance of immediately granting a Medal.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | war_effort_passive |
| Type | Utility |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"war_effort\"",
  "RelativePosition": "new Vector2Int(45, 225)",
  "CostMultiplier": "6.0",
  "IconName": "\"Icons_125\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3WarEffort.cs:34`
- `Assets.Source.Player/TechNode.cs:1`
