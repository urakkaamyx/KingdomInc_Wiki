# Red Tape Specialist

Unlocks the Bureaucrat upgrade to passively generate Requisition.

## Research effect

Unlocks the Bureaucrat upgrade to passively generate Requisition.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_passive |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |
| [Shrewd Agent](tech-requisition_office_automation_2.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"requisition_office_automation_2\"",
  "AdditionalRequirements": "new List<string> { \"war_effort\" }",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons_124\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"RequisitionOffice\", \"ReqPassive\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:42`
- `Assets.Source.Player/TechNode.cs:1`
