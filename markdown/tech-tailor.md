# Tailor

Crafts clothing and other cloth goods from a variety of fabrics.

## Research effect

Crafts clothing and other cloth goods from a variety of fabrics.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tailor |
| Type | Flow Element |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Requisition Office](tech-requisition_office.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Linen Padding](tech-linen_padding.md) |

## Leads to

| Research |
| --- |
| [Supply Linen Cloth](tech-supply_linen_cloth.md) |
| [Linen Padding](tech-linen_padding.md) |
| [Simple Robe](tech-simple_robe.md) |
| [Initiate's Hat](tech-initiate_hat.md) |
| [Linen Cloth](tech-linen_cloth.md) |
| [Cotton Cloth](tech-cotton_cloth.md) |
| [Scholar's Robe](tech-cotton_robe.md) |
| [Scholar's Hat](tech-cotton_hat.md) |
| [Witch Robe](tech-witch_robe.md) |
| [Witch Hood](tech-witch_hood.md) |
| [Animated Scissors](tech-tailor_automation.md) |
| [Tailor · second add-on slot](tech-tailor_automation_2.md) |
| [Tailor · overseers](tech-tailor_productivity.md) |
| [Tailor · artisans](tech-tailor_quality.md) |
| [Tailor · third add-on slot](tech-tailor_automation_3.md) |
| [Carpenter](tech-carpenter.md) |
| [Leatherworker](tech-leatherworker.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"requisition_office\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_38\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"linen_padding\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Tailor.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
