# Mana Superconductors

Reduces mana cost of teleporting items by 50%.

## Research effect

Reduces mana cost of teleporting items by 50%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | portal_cost_reduce |
| Type | Utility |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Portal](tech-portal.md) |

## Leads to

| Research |
| --- |
| [Stable Wormhole](tech-portal_cost_reduce_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"portal\"",
  "RelativePosition": "new Vector2Int(-45, 207)",
  "IconName": "\"Icons_162\"",
  "CostCurrency": "CurrencyCollection.GoldMana"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:133`
- `Assets.Source.Player/TechNode.cs:1`
