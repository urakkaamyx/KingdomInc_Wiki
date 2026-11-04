# Elixir of Fire Resistance

Elixir of Fire Resistance is a tier 5 resource research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_fire_resist_potion |
| Type | Resource |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Dungeon](tech-dungeon.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Elixir of Fire Resistance](item-fire_resist_potion.md) | 9999.0 |

<details><summary>Implementation fields</summary>

```json
{
  "Name": "\"@fire_resist_potion\"",
  "Description": "\"@fire_resist_potion_desc\"",
  "NodeType": "TechNodeType.Resource",
  "Root": "\"adventure_supplies\"",
  "IconName": "\"Icons2_146\"",
  "AdditionalRequirements": "new List<string> { \"dungeon\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"fire_resist_potion\", 9999.0);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:70`
- `Assets.Source.Player/TechNode.cs:1`
