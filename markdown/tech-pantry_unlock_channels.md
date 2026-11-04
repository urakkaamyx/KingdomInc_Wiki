# Deep Cavern Storage

Unlocks Pantry Channels, allowing you to store and retrieve items from eight separate containers.

## Research effect

Unlocks Pantry Channels, allowing you to store and retrieve items from eight separate containers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | pantry_unlock_channels |
| Type | Utility |
| Cost tier | 7 |
| Visibility | Hidden by code |

## Prerequisites

| Required research |
| --- |
| [Pantry](tech-pantry.md) |
| [Portal](tech-portal.md) |

<details><summary>Implementation fields</summary>

```json
{
  "Hidden": "(GamePlayer ply) => true",
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"pantry\"",
  "RelativePosition": "new Vector2Int(225, -30)",
  "IconName": "\"Icons_147\"",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "CostMultiplier": "2.0",
  "AdditionalRequirements": "new List<string> { \"portal\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:88`
- `Assets.Source.Player/TechNode.cs:1`
