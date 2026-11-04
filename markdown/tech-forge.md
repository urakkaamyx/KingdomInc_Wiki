# Forge

Smelts raw ore into pure metal bars.

## Research effect

Smelts raw ore into pure metal bars.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forge |
| Type | Flow Element |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |

## Leads to

| Research |
| --- |
| [Iron Ingot](tech-iron_ingot.md) |
| [Gold Ingot](tech-gold_ingot.md) |
| [Silver Ingot](tech-silver_ingot.md) |
| [Forge Attendant](tech-forge_automation.md) |
| [Forge · second add-on slot](tech-forge_automation_2.md) |
| [Forge · overseers](tech-forge_productivity.md) |
| [Forge · artisans](tech-forge_quality.md) |
| [Forge · third add-on slot](tech-forge_automation_3.md) |
| [Item Shop](tech-shop.md) |
| [Blacksmith](tech-blacksmith.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"mine\"",
  "RelativePosition": "new Vector2Int(630, 0)",
  "IconName": "\"Icons_15\"",
  "CostMultiplier": "0.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Forge.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
