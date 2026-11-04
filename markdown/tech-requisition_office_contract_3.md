# Overseas Export

Adds another Contract slot to your Requisition Office.

## Research effect

Adds another Contract slot to your Requisition Office.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_contract_3 |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |
| [Contractual Obligations](tech-requisition_office_contract.md) |
| [Adventurer's Guild](tech-adventurers_guild.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"requisition_office_contract\"",
  "RelativePosition": "new Vector2Int(0, -180)",
  "CostTier": "5",
  "IconName": "\"Icons_36\"",
  "AdditionalRequirements": "new List<string> { \"adventurers_guild\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tRequisitionOffice.AddRequisitionContract();\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:85`
- `Assets.Source.Player/TechNode.cs:1`
