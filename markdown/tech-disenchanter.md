# Disenchanter

Manipulates the magical energy of high-quality weapons and armor to extract their Mana. Supplied items are destroyed in the process.

## Research effect

Manipulates the magical energy of high-quality weapons and armor to extract their Mana. Supplied items are destroyed in the process.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | disenchanter |
| Type | Flow Element |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |

## Leads to

| Research |
| --- |
| [Mana Vacuum](tech-disenchanter_automation.md) |
| [Annihilation](tech-disenchanter_mana.md) |
| [Disenchanter · second add-on slot](tech-disenchanter_automation_2.md) |
| [Aether Collector](tech-disenchanter_passive.md) |
| [Disenchanter · third add-on slot](tech-disenchanter_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"enchanter\"",
  "RelativePosition": "new Vector2Int(630, 0)",
  "IconName": "\"Icons_156\"",
  "CostMultiplier": "1.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Disenchanter.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
