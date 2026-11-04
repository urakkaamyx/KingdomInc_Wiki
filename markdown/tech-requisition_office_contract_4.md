# Extradimensional Export

Adds another Contract slot to your Requisition Office.

## Research effect

Adds another Contract slot to your Requisition Office.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_contract_4 |
| Type | Utility |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |
| [Mass Requisition](tech-requisition_office_contract_2.md) |
| [Enchanter](tech-enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"requisition_office_contract_2\"",
  "RelativePosition": "new Vector2Int(0, -180)",
  "CostTier": "6",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "IconName": "\"Icons_36\"",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tRequisitionOffice.AddRequisitionContract();\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:98`
- `Assets.Source.Player/TechNode.cs:1`
