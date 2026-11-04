# Requisition Office

Demands a specific item and converts it into Requisition currency.

## Research effect

Demands a specific item and converts it into Requisition currency.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office |
| Type | Flow Element |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |

## Leads to

| Research |
| --- |
| [Mine Sapphire](tech-mine_sapphire.md) |
| [Clone Tool](tech-clone_tool.md) |
| [Requisition Officer](tech-requisition_office_automation.md) |
| [Agent](tech-requisition_office_cashier.md) |
| [Requisition Office · second add-on slot](tech-requisition_office_automation_2.md) |
| [Requisition Office · third add-on slot](tech-requisition_office_automation_3.md) |
| [Red Tape Specialist](tech-requisition_office_passive.md) |
| [Reroll Contract](tech-requisition_office_reroll.md) |
| [Contractual Obligations](tech-requisition_office_contract.md) |
| [Mass Requisition](tech-requisition_office_contract_2.md) |
| [Overseas Export](tech-requisition_office_contract_3.md) |
| [Extradimensional Export](tech-requisition_office_contract_4.md) |
| [Inspector](tech-inspector.md) |
| [Incinerator](tech-incinerator.md) |
| [Quick Upgrade](tech-easy_node_upgrade.md) |
| [Item List View](tech-item_list.md) |
| [Tailor](tech-tailor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"supply_depot\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_33\"",
  "CostTier": "2",
  "CostCurrency": "CurrencyCollection.Gold",
  "CostMultiplier": "3.0",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tRequisitionOffice.AddRequisitionContract();\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:13`
- `Assets.Source.Player/TechNode.cs:1`
