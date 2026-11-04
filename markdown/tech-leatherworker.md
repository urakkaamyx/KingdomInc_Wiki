# Leatherworker

Crafts leather armor that provides both flexibility and adequate protection.

## Research effect

Crafts leather armor that provides both flexibility and adequate protection.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | leatherworker |
| Type | Flow Element |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Rough String](tech-rough_string.md) |

## Leads to

| Research |
| --- |
| [Supply Rough Leather](tech-supply_rough_leather.md) |
| [Rough String](tech-rough_string.md) |
| [Rough Vest](tech-rough_vest.md) |
| [Rough Leather Hat](tech-rough_leather_hat.md) |
| [Rough Leather](tech-rough_leather.md) |
| [Supple String](tech-supple_string.md) |
| [Embossed Vest](tech-embossed_vest.md) |
| [Embossed Mask](tech-embossed_hat.md) |
| [Primal String](tech-primal_string.md) |
| [Primal Cover](tech-primal_cover.md) |
| [Primal Mask](tech-primal_mask.md) |
| [Honest Craftmanship](tech-leatherworker_automation.md) |
| [Leatherworker · second add-on slot](tech-leatherworker_automation_2.md) |
| [Leatherworker · overseers](tech-leatherworker_productivity.md) |
| [Leatherworker · artisans](tech-leatherworker_quality.md) |
| [Leatherworker · third add-on slot](tech-leatherworker_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"tailor\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_39\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"rough_string\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T2Leatherworker.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
