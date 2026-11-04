# Glass Vial

An empty sterilized vessel used in the creation of potions.

## Research effect

An empty sterilized vessel used in the creation of potions.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | glass_vial |
| Type | Resource |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Alchemist](tech-alchemist.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Glass Vial](item-glass_vial.md) | 9999.0 |

## Related item

| Item |
| --- |
| [Glass Vial](item-glass_vial.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"adventure_supplies\"",
  "IconName": "\"Icons_223\"",
  "CostTier": "8",
  "AdditionalRequirements": "new List<string> { \"alchemist\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"glass_vial\", 9999.0);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:97`
- `Assets.Source.Player/TechNode.cs:1`
