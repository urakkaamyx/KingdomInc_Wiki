# Foreign Legion

Enables the export of conscripts and soldiers at the Mercenary Guild.

## Research effect

Enables the export of conscripts and soldiers at the Mercenary Guild.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mercenary_conscripts |
| Type | Utility |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Mercenary Guild](tech-mercenary_guild.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"mercenary_guild\"",
  "RelativePosition": "new Vector2Int(-225, -64)",
  "IconName": "\"Icons_181\"",
  "CostCurrency": "CurrencyCollection.GoldDucat",
  "CostMultiplier": "2.0"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:134`
- `Assets.Source.Player/TechNode.cs:1`
