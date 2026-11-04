# Inspector

Allows you to inspect the stats of the last item that passed through this node.

## Research effect

Allows you to inspect the stats of the last item that passed through this node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | inspector |
| Type | Flow Element |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"requisition_office\"",
  "RelativePosition": "new Vector2Int(450, 17)",
  "IconName": "\"Icons_37\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:112`
- `Assets.Source.Player/TechNode.cs:1`
