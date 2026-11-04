# Common Ground

The Guildhouse can now also be used to house non-adventurer humans.

## Research effect

The Guildhouse can now also be used to house non-adventurer humans.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | guildhouse_conscripts |
| Type | Utility |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Guildhouse](tech-guildhouse.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"guildhouse\"",
  "RelativePosition": "new Vector2Int(-225, 26)",
  "IconName": "\"Icons_61\"",
  "CostCurrency": "CurrencyCollection.GoldCrown",
  "CostMultiplier": "2.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:117`
- `Assets.Source.Player/TechNode.cs:1`
