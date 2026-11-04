# Portal

Enables instantaneous transport of items over long distances and between workspaces. Consumes a small amount of Mana.

## Research effect

Enables instantaneous transport of items over long distances and between workspaces. Consumes a small amount of Mana.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | portal |
| Type | Flow Element |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |

## Leads to

| Research |
| --- |
| [Extradimensional Storage Space](tech-armory_unlock_channels.md) |
| [Mana Superconductors](tech-portal_cost_reduce.md) |
| [Multidimensional Transportation](tech-portal_unlock_channels.md) |
| [Deep Cavern Storage](tech-pantry_unlock_channels.md) |
| [Endless Hall of Doors](tech-guildhouse_unlock_channels.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"farm\"",
  "RelativePosition": "new Vector2Int(-450, 17)",
  "IconName": "\"Icons_183\"",
  "CostCurrency": "CurrencyCollection.GoldMana"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:125`
- `Assets.Source.Player/TechNode.cs:1`
