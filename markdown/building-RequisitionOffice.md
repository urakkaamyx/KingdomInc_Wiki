# Requisition Office

Demands a specific item and converts it into Requisition currency.

## Purpose

Demands a specific item and converts it into Requisition currency.

## Building reference

| Property | Value |
| --- | --- |
| Type | RequisitionOffice |
| Category | Consumption |
| Inheritance | RequisitionOffice → FlowElement |
| Research required | [Requisition Office](tech-requisition_office.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Requisition Officer](tech-requisition_office_automation.md) | 2 |
| [Requisition Office · second add-on slot](tech-requisition_office_automation_2.md) | 3 |
| [Requisition Office · third add-on slot](tech-requisition_office_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Requisition Office |
| Icon Name | Icons 33 |
| Music Track | Mystical Lands LOOP BPM110 |
| Category | ElementCategory.Consumption |
| Icon | ContractedItem?.GetIcon() ?? base.Icon |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "RequisitionOffice",
  "Inherited behavior": "RequisitionOffice → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/RequisitionOffice.cs:14`
