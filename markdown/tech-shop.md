# Item Shop

Sells most items on the open market for a fair price.

## Research effect

Sells most items on the open market for a fair price.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shop |
| Type | Flow Element |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Forge](tech-forge.md) |

## Leads to

| Research |
| --- |
| [Future Proofing](tech-shop_expansion.md) |
| [Shop Attendant](tech-shop_automation.md) |
| [Cashier](tech-shop_cashier.md) |
| [Item Shop · second add-on slot](tech-shop_automation_2.md) |
| [Item Shop coffers](tech-shop_coffers.md) |
| [Item Shop · third add-on slot](tech-shop_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"forge\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_3\"",
  "CostMultiplier": "0.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Shop.cs:12`
- `Assets.Source.Player/TechNode.cs:1`
