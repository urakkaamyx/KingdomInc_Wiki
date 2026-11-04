# Incinerator

Destroys any unwanted items that are inserted into its input.

## Research effect

Destroys any unwanted items that are inserted into its input.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | incinerator |
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
  "RelativePosition": "new Vector2Int(-450, 17)",
  "IconName": "\"Icons_57\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:119`
- `Assets.Source.Player/TechNode.cs:1`
