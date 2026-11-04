# Butcher

Magically transforms the animals from your farm into delicious meat and useful leather.

## Research effect

Magically transforms the animals from your farm into delicious meat and useful leather.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | butcher |
| Type | Flow Element |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Butcher Cattle](tech-butcher_cattle.md) |

## Leads to

| Research |
| --- |
| [The Meat Man](tech-butcher_automation.md) |
| [Butcher · second add-on slot](tech-butcher_automation_2.md) |
| [Butcher · overseers](tech-butcher_productivity.md) |
| [Butcher · artisans](tech-butcher_quality.md) |
| [Butcher · third add-on slot](tech-butcher_automation_3.md) |
| [Butcher Cattle](tech-butcher_cattle.md) |
| [Butcher Salamander](tech-butcher_salamander.md) |
| [Butcher Stalker](tech-butcher_stalker.md) |
| [Anatomy Lesson](tech-cr_assassin.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"kitchen\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_186\"",
  "ForceRootNode": "true",
  "CostMultiplier": "3.5",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"butcher_cattle\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Butcher.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
