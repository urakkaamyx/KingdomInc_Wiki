# Contractual Obligations

Adds a new Contract slot to your Requisition Office.

## Research effect

Adds a new Contract slot to your Requisition Office.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_contract |
| Type | Utility |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |
| [Reroll Contract](tech-requisition_office_reroll.md) |

## Leads to

| Research |
| --- |
| [Mass Requisition](tech-requisition_office_contract_2.md) |
| [Overseas Export](tech-requisition_office_contract_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"requisition_office_reroll\"",
  "RelativePosition": "new Vector2Int(180, 0)",
  "IconName": "\"Icons_36\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tRequisitionOffice.AddRequisitionContract();\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:61`
- `Assets.Source.Player/TechNode.cs:1`
