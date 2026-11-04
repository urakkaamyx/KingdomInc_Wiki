# Stable Wormhole

Reduces mana cost of teleporting items by an additional 50%.

## Research effect

Reduces mana cost of teleporting items by an additional 50%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | portal_cost_reduce_2 |
| Type | Utility |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Mana Superconductors](tech-portal_cost_reduce.md) |
| [Inventor](tech-inventor.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"portal_cost_reduce\"",
  "RelativePosition": "new Vector2Int(-180, 0)",
  "IconName": "\"Icons2_91\"",
  "CostTier": "11",
  "AdditionalRequirements": "new List<string> { \"inventor\" }",
  "CostCurrency": "CurrencyCollection.GoldIngenuity"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:141`
- `Assets.Source.Player/TechNode.cs:1`
