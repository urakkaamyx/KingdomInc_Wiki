# Extradimensional Storage Space

Unlocks Channels, allowing all global storage nodes to store and retrieve items from eight separate containers.

## Research effect

Unlocks Channels, allowing all global storage nodes to store and retrieve items from eight separate containers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | armory_unlock_channels |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Armory](tech-armory.md) |
| [Portal](tech-portal.md) |

## Leads to

| Research |
| --- |
| [Overflowing Armory](tech-armory_overflow.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"armory\"",
  "RelativePosition": "new Vector2Int(-45, -242)",
  "IconName": "\"Icons_147\"",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "CostMultiplier": "2.0",
  "AdditionalRequirements": "new List<string> { \"portal\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:117`
- `Assets.Source.Player/TechNode.cs:1`
