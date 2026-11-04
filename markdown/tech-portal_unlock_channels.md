# Multidimensional Transportation

Unlocks Portal Indexes, giving each Portal channel an additional eight sub-channels.

## Research effect

Unlocks Portal Indexes, giving each Portal channel an additional eight sub-channels.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | portal_unlock_channels |
| Type | Utility |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Portal](tech-portal.md) |

## Leads to

| Research |
| --- |
| [Overflowing Portal](tech-portal_overflow.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"portal\"",
  "RelativePosition": "new Vector2Int(-45, -242)",
  "IconName": "\"Icons_147\"",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "CostMultiplier": "2.0",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (Portal element in ply.GetElements<Portal>())\n\t\t\t\t{\n\t\t\t\t\telement.World.GetComponent<WorldFlowPortal>().UpdateChannel();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:151`
- `Assets.Source.Player/TechNode.cs:1`
