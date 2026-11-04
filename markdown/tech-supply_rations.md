# Rations

Rations is a tier 5 resource research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_rations |
| Type | Resource |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Rations](item-rations.md) | 9999.0 |

<details><summary>Implementation fields</summary>

```json
{
  "Name": "\"@rations\"",
  "Description": "\"@rations_desc\"",
  "NodeType": "TechNodeType.Resource",
  "Root": "\"adventure_supplies\"",
  "IconName": "\"Icons_220\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"rations\", 9999.0);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:48`
- `Assets.Source.Player/TechNode.cs:1`
