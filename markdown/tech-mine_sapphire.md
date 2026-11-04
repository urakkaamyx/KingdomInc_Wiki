# Mine Sapphire

A rich vein of gemstones provides a steady supply of Sapphires.

## Research effect

A rich vein of gemstones provides a steady supply of Sapphires.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_sapphire |
| Type | Resource |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |
| [Requisition Office](tech-requisition_office.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Sapphire](item-sapphire.md) | 0.2 |

## Leads to

| Research |
| --- |
| [Sapphire Crown](tech-gold_crown.md) |
| [Initiate's Staff](tech-initiate_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"mine\"",
  "IconName": "\"Icons_69\"",
  "CostTier": "2",
  "AdditionalRequirements": "new List<string> { \"requisition_office\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"sapphire\", 0.2);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Mine.cs:37`
- `Assets.Source.Player/TechNode.cs:1`
