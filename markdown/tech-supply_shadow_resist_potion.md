# Elixir of Shadow Resistance

Elixir of Shadow Resistance is a tier 8 resource research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_shadow_resist_potion |
| Type | Resource |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Dungeon](tech-dungeon.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Elixir of Shadow Resistance](item-shadow_resist_potion.md) | 9999.0 |

<details><summary>Implementation fields</summary>

```json
{
  "Name": "\"@shadow_resist_potion\"",
  "Description": "\"@shadow_resist_potion_desc\"",
  "NodeType": "TechNodeType.Resource",
  "Root": "\"adventure_supplies\"",
  "IconName": "\"Icons2_183\"",
  "CostTier": "8",
  "AdditionalRequirements": "new List<string> { \"dungeon\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"shadow_resist_potion\", 9999.0);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:83`
- `Assets.Source.Player/TechNode.cs:1`
