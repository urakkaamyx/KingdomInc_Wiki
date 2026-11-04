# Switch

Allows you to manually turn parts of your workflow on or off.

## Research effect

Allows you to manually turn parts of your workflow on or off.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | track_switch |
| Type | Flow Element |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Track Switch](tech-track_switch_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "CostMultiplier": "0.5",
  "Previous": "\"war_effort\"",
  "RelativePosition": "new Vector2Int(450, -107)",
  "IconName": "\"Icons_73\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3WarEffort.cs:50`
- `Assets.Source.Player/TechNode.cs:1`
