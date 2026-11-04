# Reroll Contract

Allows you to switch out your Requisition contracts in case you want to deliver other items.

## Research effect

Allows you to switch out your Requisition contracts in case you want to deliver other items.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_reroll |
| Type | Utility |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |

## Leads to

| Research |
| --- |
| [Contractual Obligations](tech-requisition_office_contract.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"requisition_office\"",
  "RelativePosition": "new Vector2Int(405, 45)",
  "IconName": "\"Icons_35\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:54`
- `Assets.Source.Player/TechNode.cs:1`
