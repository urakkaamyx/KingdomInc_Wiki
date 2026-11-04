# Collector

Takes in inputs from multiple connected nodes in turn, and combines them into a single output.

## Research effect

Takes in inputs from multiple connected nodes in turn, and combines them into a single output.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | collector |
| Type | Flow Element |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Distributor](tech-distributor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"distributor\"",
  "RelativePosition": "new Vector2Int(270, 0)",
  "IconName": "\"Icons_28\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1SupplyDepot.cs:77`
- `Assets.Source.Player/TechNode.cs:1`
