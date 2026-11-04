# Animated Workforce

Reduces the cost of recruiting new Forest workers by 25%.

## Research effect

Reduces the cost of recruiting new Forest workers by 25%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_workforce |
| Type | Utility |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |
| [Enchanter](tech-enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"forest\"",
  "IconName": "\"Icons2_167\"",
  "CostTier": "6",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }",
  "RelativePosition": "new Vector2Int(45, 225)"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:40`
- `Assets.Source.Player/TechNode.cs:1`
