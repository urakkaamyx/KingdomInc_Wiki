# Endless Hall of Doors

Unlocks Guildhouse Channels, allowing you to store and retrieve adventurers from eight separate containers.

## Research effect

Unlocks Guildhouse Channels, allowing you to store and retrieve adventurers from eight separate containers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | guildhouse_unlock_channels |
| Type | Utility |
| Cost tier | 8 |
| Visibility | Hidden by code |

## Prerequisites

| Required research |
| --- |
| [Guildhouse](tech-guildhouse.md) |
| [Portal](tech-portal.md) |

<details><summary>Implementation fields</summary>

```json
{
  "Hidden": "(GamePlayer ply) => true",
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"guildhouse\"",
  "RelativePosition": "new Vector2Int(-225, 26)",
  "IconName": "\"Icons_147\"",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "CostMultiplier": "2.0",
  "AdditionalRequirements": "new List<string> { \"portal\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:106`
- `Assets.Source.Player/TechNode.cs:1`
