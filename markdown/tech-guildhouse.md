# Guildhouse

A place for your adventurers to catch their breath. All guildhouses are linked and contents can be accessed from anywhere.

## Research effect

A place for your adventurers to catch their breath. All guildhouses are linked and contents can be accessed from anywhere.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | guildhouse |
| Type | Flow Element |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Endless Hall of Doors](tech-guildhouse_unlock_channels.md) |
| [Common Ground](tech-guildhouse_conscripts.md) |
| [Mercenary Guild](tech-mercenary_guild.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"dungeon\"",
  "RelativePosition": "new Vector2Int(-450, 17)",
  "IconName": "\"Icons_196\"",
  "CostCurrency": "CurrencyCollection.GoldCrown"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:98`
- `Assets.Source.Player/TechNode.cs:1`
