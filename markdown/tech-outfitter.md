# Outfitter

Equips your combatants with a single piece of equipment crafted in your kingdom.

## Research effect

Equips your combatants with a single piece of equipment crafted in your kingdom.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | outfitter |
| Type | Flow Element |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Barracks](tech-barracks.md) |

## Leads to

| Research |
| --- |
| [Self Service](tech-outfitter_automation.md) |
| [New Hotness](tech-outfitter_skip_replace.md) |
| [Bring A Snack](tech-outfitter_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"barracks\"",
  "RelativePosition": "new Vector2Int(-450, 17)",
  "CostCurrency": "CurrencyCollection.GoldRequisition",
  "IconName": "\"Icons_62\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Barracks.cs:33`
- `Assets.Source.Player/TechNode.cs:1`
