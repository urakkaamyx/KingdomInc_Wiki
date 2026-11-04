# Button

Adds a manual control to your workflow. One button click allows one item to pass through.

## Research effect

Adds a manual control to your workflow. One button click allows one item to pass through.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | single_button |
| Type | Flow Element |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "CostMultiplier": "0.5",
  "Previous": "\"war_effort\"",
  "RelativePosition": "new Vector2Int(450, 107)",
  "IconName": "\"Icons_74\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3WarEffort.cs:42`
- `Assets.Source.Player/TechNode.cs:1`
