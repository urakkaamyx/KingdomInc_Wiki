# Requisition Office · second add-on slot

Requisition Office · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |
| [Requisition Officer](tech-requisition_office_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Requisition Office · third add-on slot](tech-requisition_office_automation_3.md) |
| [Red Tape Specialist](tech-requisition_office_passive.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"RequisitionOffice\", \"callSource\": \"source/Assets.Source.Player.Tech/T2RequisitionOffice.cs\", \"callLine\": 40, \"id\": \"requisition_office_automation_2\", \"previous\": \"requisition_office_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Requisition Office · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"requisition_office\", \"requires\": [\"requisition_office\", \"requisition_office_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:40`
