# Requisition Officer

Unlocks the first Upgrade slot for your Requisition Office.

Unlocks the Worker upgrade to automatically submit requisitioned items.

## Research effect

Unlocks the first Upgrade slot for your Requisition Office.

Unlocks the Worker upgrade to automatically submit requisitioned items.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | requisition_office_automation |
| Type | Upgrade Slot |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |

## Leads to

| Research |
| --- |
| [Agent](tech-requisition_office_cashier.md) |
| [Requisition Office · second add-on slot](tech-requisition_office_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"RequisitionOffice\", \"callSource\": \"source/Assets.Source.Player.Tech/T2RequisitionOffice.cs\", \"callLine\": 27, \"id\": \"requisition_office_automation\", \"root\": \"requisition_office\", \"tier\": 2, \"name\": \"Requisition Officer\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"requisition_office\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2RequisitionOffice.cs:27`
