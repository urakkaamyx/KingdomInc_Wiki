# Mass Requisition

Adds another Contract slot to your Requisition Office.

## Research effect

Adds another Contract slot to your Requisition Office.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_contract_2 |
| Type | Utility |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |
| [Contractual Obligations](tech-requisition_office_contract.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Extradimensional Export](tech-requisition_office_contract_4.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"requisition_office_contract\"",
  "RelativePosition": "new Vector2Int(180, 0)",
  "CostTier": "4",
  "IconName": "\"Icons_36\"",
  "AdditionalRequirements": "new List<string> { \"war_effort\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tRequisitionOffice.AddRequisitionContract();\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:72`
- `Assets.Source.Player/TechNode.cs:1`
