# Healing Potion

Healing Potion is a tier 5 resource research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_healing_potion |
| Type | Resource |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Healing Potion](item-healing_potion.md) | 9999.0 |

<details><summary>Implementation fields</summary>

```json
{
  "Name": "\"@healing_potion\"",
  "Description": "\"@healing_potion_desc\"",
  "NodeType": "TechNodeType.Resource",
  "Root": "\"adventure_supplies\"",
  "IconName": "\"Icons_219\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"healing_potion\", 9999.0);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:24`
- `Assets.Source.Player/TechNode.cs:1`
