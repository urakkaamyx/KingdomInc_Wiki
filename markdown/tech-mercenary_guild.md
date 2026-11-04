# Mercenary Guild

Export the services of your adventurers by selling their contracts to a foreign mercenary company.

## Research effect

Export the services of your adventurers by selling their contracts to a foreign mercenary company.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mercenary_guild |
| Type | Flow Element |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Guildhouse](tech-guildhouse.md) |

## Leads to

| Research |
| --- |
| [Foreign Legion](tech-mercenary_conscripts.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"guildhouse\"",
  "RelativePosition": "new Vector2Int(0, 270)",
  "IconName": "\"Icons_200\"",
  "CostCurrency": "CurrencyCollection.GoldDucat"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:126`
- `Assets.Source.Player/TechNode.cs:1`
