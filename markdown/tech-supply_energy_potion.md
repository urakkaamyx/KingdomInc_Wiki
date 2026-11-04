# Revitalizing Potion

Revitalizing Potion is a tier 5 resource research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_energy_potion |
| Type | Resource |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Revitalizing Potion](item-energy_potion.md) | 9999.0 |

<details><summary>Implementation fields</summary>

```json
{
  "Name": "\"@energy_potion\"",
  "Description": "\"@energy_potion_desc\"",
  "NodeType": "TechNodeType.Resource",
  "Root": "\"adventure_supplies\"",
  "IconName": "\"Icons2_194\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"energy_potion\", 9999.0);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:36`
- `Assets.Source.Player/TechNode.cs:1`
