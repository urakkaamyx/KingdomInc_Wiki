# Min Max

Equipment can have one enhancement of each type (Enchanted, Engraved, etc.) instead of just one in total.

## Research effect

Equipment can have one enhancement of each type (Enchanted, Engraved, etc.) instead of just one in total.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enhance_multiple |
| Type | Utility |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"enchanter\"",
  "RelativePosition": "new Vector2Int(405, 45)",
  "IconName": "\"Icons2_51\"",
  "CostMultiplier": "6.0",
  "CostCurrency": "CurrencyCollection.GoldMana"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:20`
- `Assets.Source.Player/TechNode.cs:1`
