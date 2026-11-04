# Quick Upgrade

Control-click an empty node upgrade slot to automatically purchase the most relevant upgrade.

## Research effect

Control-click an empty node upgrade slot to automatically purchase the most relevant upgrade.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | easy_node_upgrade |
| Type | Utility |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"requisition_office\"",
  "RelativePosition": "new Vector2Int(-315, -135)",
  "IconName": "\"Icons_18\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:126`
- `Assets.Source.Player/TechNode.cs:1`
