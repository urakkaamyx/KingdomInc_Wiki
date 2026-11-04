# Distributor

Takes in a single input, and distributes its items equally to multiple outputs.

## Research effect

Takes in a single input, and distributes its items equally to multiple outputs.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | distributor |
| Type | Flow Element |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |

## Leads to

| Research |
| --- |
| [Collector](tech-collector.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"supply_depot\"",
  "RelativePosition": "new Vector2Int(450, 107)",
  "IconName": "\"Icons_29\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1SupplyDepot.cs:70`
- `Assets.Source.Player/TechNode.cs:1`
