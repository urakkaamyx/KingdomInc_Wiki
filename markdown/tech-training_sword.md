# Training Sword

A basic wooden sword. Not made for actual combat, but widely available and surprisingly sturdy.

## Research effect

A basic wooden sword. Not made for actual combat, but widely available and surprisingly sturdy.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_sword |
| Type | Resource |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Training Sword](item-training_sword.md) | 9999.0 |

## Related item

| Item |
| --- |
| [Training Sword](item-training_sword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Resource",
  "Root": "\"adventure_supplies\"",
  "IconName": "\"Icons2_75\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"training_sword\", 9999.0);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:60`
- `Assets.Source.Player/TechNode.cs:1`
