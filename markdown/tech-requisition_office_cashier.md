# Agent

Unlocks a new Upgrade for your Requisition Office.

Increases the amount of Requisition earned by {0}.

## Research effect

Unlocks a new Upgrade for your Requisition Office.

Increases the amount of Requisition earned by {0}.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_cashier |
| Type | Upgrade Slot |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |
| [Requisition Officer](tech-requisition_office_automation.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"requisition_office_automation\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "Description": "Translation.TranslateOnly(\"@requisition_office_cashier_desc\", GameMath.FormatPercentage(0.10000000149011612))",
  "IconName": "\"Icons_119\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"RequisitionOffice\", \"ReqCashier\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
