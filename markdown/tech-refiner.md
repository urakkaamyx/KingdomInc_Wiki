# Refiner

Improves the Quality of inserted items by up to 10%. A percentage of items are destroyed in the process, especially at high quality.

## Research effect

Improves the Quality of inserted items by up to 10%. A percentage of items are destroyed in the process, especially at high quality.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | refiner |
| Type | Flow Element |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |

## Leads to

| Research |
| --- |
| [Flash of Brilliance](tech-critical_craft.md) |
| [Mana Sculptor](tech-refiner_mana.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"enchanter\"",
  "RelativePosition": "new Vector2Int(90, -254)",
  "IconName": "\"Icons_157\"",
  "CostMultiplier": "2.0",
  "CostCurrency": "CurrencyCollection.GoldMana"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:151`
- `Assets.Source.Player/TechNode.cs:1`
